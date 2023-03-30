const keygen_button = document.getElementById("priv-key");
const res_area = document.getElementById("res");
const ciphertext_res = document.getElementById("ciphertext")
const steps = document.getElementById("steps");
const pt_form = document.querySelector("form");
let data;

const assoc = {
    "modulus": "Modulus (n)",
    "publicExponent": "Public exponent (e)",
    "privateExponent": "Private Exponent (d)",
    "prime1": "Prime 1 (p)",
    "prime2": "Prime 2 (q)",
    "exponent1": "d modulo p-1",
    "exponent2": "d modulo q-1",
    "coefficient": "Inverse of q modulo p",
    "Private-Key": "Modulus bits"

}

if(pt_form) {
    pt_form.addEventListener("submit", (e) => {
        e.preventDefault();
        let text = document.getElementById("plaintext").value;
        getEncryption(text, displayCipherText);
    })
}

if (keygen_button){
    keygen_button.addEventListener("click", (e) => {
        e.preventDefault();
        console.log("pressed")
        getData(displayData);
    });
}

function generateTable(table, data) {
    data = data
    let keys = Object.keys(data)

    for (let element of keys) {
      let row = table.insertRow();
      let cell = row.insertCell();
      let text = document.createTextNode(assoc[element]);
      cell.appendChild(text);

      cell = row.insertCell();
      text = document.createTextNode(data[element]);
      cell.appendChild(text);
    }
  }

function displayCipherText(c){
    ciphertext_res.innerHTML += `${c}`
}

function displayData(data) {
    let dat = JSON.parse(data)
    let t = document.querySelector("table");

    generateTable(t, dat)
}

function getData(callback) {
    const request = new XMLHttpRequest();
    request.onreadystatechange = () => {
        if (request.readyState === 4) {
        callback(request.response);
        }
    };
    request.open("POST", "/keygen");
    request.send();
}

function getEncryption(url, callback){
    fetch(url).then(function(response) {
        return response;
      }).then(callback(data))
      .catch(function(err) {
        console.log('Fetch Error :-S', err);
      });
}