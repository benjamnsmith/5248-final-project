const integer_form = document.querySelector("form");

integer_form.addEventListener("submit", (e) => {
    e.preventDefault();

    const txtbox = document.querySelector("#val");

    var n = txtbox.value

    txt = encrypt(txt);
})




function getData(callback) {
    const request = new XMLHttpRequest();
    request.onreadystatechange = () => {
        if (request.readyState === 4) {
        callback(request.response);
        }
    };
    request.open("POST", "/ecc/pollard");
    request.send();
}