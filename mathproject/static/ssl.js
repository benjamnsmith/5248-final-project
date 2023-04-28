const keygen_button = document.getElementById("priv-key");
const res_area = document.getElementById("col2");
const ciphertext_res = document.getElementById("ciphertext")
const steps = document.getElementById("steps");
const step3button = document.querySelector("#trigger-3");
const step2 = document.querySelector("#step2");
const step3 = document.querySelector("#step3");

step2.style.display = "none";
step3.style.display = "none";
res_area.style.display = "none";

/* TODO:
*  Setup server to encrypt datatgram
*  Find a datagram
*  Show encrypted datagram
*/
let data;

const assoc = {
    "modulus": "Modulus ($n$)",
    "publicExponent": "Public exponent ($e$)",
    "privateExponent": "Private Exponent ($d$)",
    "prime1": "Prime 1 ($p$)",
    "prime2": "Prime 2 ($q$)",
    "exponent1": "$d \\text{ modulo } p-1$",
    "exponent2": "$d \\text{ modulo } q-1$",
    "coefficient": "$q^{-1}$ modulo $p$",
    "Private-Key": "Modulus bits"

}

if(step3button) {
    step3button.addEventListener("click", (e) => {
        e.preventDefault();
        getEncryption(displayCipherText);
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

    res_area.style.width = "100%";
    MathJax.typeset()
  }

function displayCipherText(c){
    step3.style.display = "list-item";
    ciphertext_res.innerHTML += `${c}`
}

function displayData(data) {
    let dat = JSON.parse(data)
    let t = document.querySelector("table");
    res_area.style.display = "block";

    generateTable(t, dat);

    step2.style.display = "list-item";
}

function getData(callback) {
    const request = new XMLHttpRequest();
    request.onreadystatechange = () => {
        if (request.readyState === 4) {
        callback(request.response);
        }
    };
    request.open("POST", "/rsa/keygen");
    request.send();
}

function getEncryption(callback) {
    const request = new XMLHttpRequest();
    request.onreadystatechange = () => {
        if (request.readyState === 4) {
        callback(request.response);
        }
    };
    request.open("POST", "/rsa/rsa-encrypt");
    request.send();
}