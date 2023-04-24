const frm = document.querySelector("form");
const alg = document.querySelector("#factoring_alg");
const btn = document.querySelector("button");
const quantum_section = document.querySelector(".quantum");
const classical_section = document.querySelector(".classical");

var shor = 1;
var classical = 1;
const MAX = 1000;


function update() {

    var count_c = document.querySelector("#count_c");
    var count_q = document.querySelector("#count_q");

    shor *= 2;
    classical += 1;

    count_c.innerText = classical ;
    count_q.innerText = shor ;

    if (shor >= MAX) {
        alert("Done")
        resetAnimation();
    } else {
        setTimeout(update, 500);
    }
}

function runAnimation(chosen_alg) {
    btn.disabled = true;

    const c = 0.2190422;

    classical_section.innerHTML = `<p>${chosen_alg} computations</p><span id="count_c"></span>`;
    quantum_section.innerHTML = `<p>Shor's Algorithm computations</p><span id="count_q"></span>`;

    setTimeout(update, 1000);
}


function resetAnimation() {
    btn.disabled = false;
    classical_section.innerText = "";
    quantum_section.innerText = "";
    shor = 1;
    classical = 1;
}

frm.addEventListener("submit", (e) => {
    e.preventDefault();
    runAnimation(alg.value);
})