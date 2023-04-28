const start_button = document.querySelector("#key-trigger")
const keyArea = document.querySelector("#key-area")


start_button.addEventListener("click", (e) => {
    e.preventDefault();
    console.log("pressed")
    getData(keyExchange)
})

function keyExchange(data){
    let dat = JSON.parse(data);
    let keys = Object.keys(dat);
    console.log(keys)

    for(var key of keys){
        keyArea.innerHTML += `<strong>${key}</strong>: ${dat[key]}<br><br>`
    }
}


function getData(callback) {
    const request = new XMLHttpRequest();
    request.onreadystatechange = () => {
        if (request.readyState === 4) {
        callback(request.response);
        }
    };
    request.open("POST", "/ecc/ecdh-keys");
    request.send();
}