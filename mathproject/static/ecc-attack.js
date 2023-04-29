const integer_form = document.querySelector("form");
const res = document.querySelector("#pollard_results");

var value = 0;

integer_form.addEventListener("submit", (e) => {
    e.preventDefault();

    res.innerHTML = "<p>Now calculating...</p>"
    const txtbox = document.querySelector("#num");

    value = txtbox.value

    getData(show, value);

})

function show(data){
    if (data == -1){
        res.innerHTML = "<p>Looks like you entered a number that was too big for my little server to factor. Try again with something smaller.</p>";
	return;
    }
    d = JSON.parse(data);
    const keys = Object.keys(d);
    console.log(keys)
    res.innerHTML = `<p>A prime factor of \$${value}\$ is \$${d['got']}\$.<br> It took Pollard's method \$${d['runs']}\$ attempts to get this value.</p>`
    MathJax.typeset();
}


function getData(callback, d) {
    const request = new XMLHttpRequest();
    request.onreadystatechange = () => {
        if (request.readyState === 4) {
        callback(request.response);
        }
    };
    request.open("POST", "/ecc/pollard");
    request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    request.send(`n=${d}`);
}
