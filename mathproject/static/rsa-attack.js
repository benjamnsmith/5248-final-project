const frm = document.querySelector("form");
const alg = document.querySelector("#factoring_alg");
const btn = document.querySelector("button");
const quantum_section = document.querySelector(".quantum");
const classical_section = document.querySelector(".classical");
const note = document.querySelector("#running_note");
var count_q = document.querySelector("#count_q");
var count_c = document.querySelector("#count_c");

var shor = 1;
var classical = 1;
var shor_factor = 2;
const MAX = 1000;
var chosen_alg = ""


function update() {

    shor += shor_factor;
    classical += 2;

    count_c.style.width = String(classical/10) + "%";
    count_q.style.width = String(shor/10) + "%";

    if (Math.floor(Math.random() * MAX) == classical){
        count_c.style.width = "100%";
        alert(`${chosen_alg} factored it first!`);
        resetAnimation();
        return
    }
    if (Math.floor(Math.random() * MAX) < MAX/4){
        shor_factor += 1;
        console.log("increasing shor factor")
    }
    if (shor >= MAX) {
        count_q.style.width = "100%";
        alert("Shor's algorithm factored it first!")
        resetAnimation();
    } else if (classical >= MAX){
        count_c.style.width = "100%";
        alert(`${chosen_alg} factored it first!`)
        resetAnimation();
    } else {
        setTimeout(update, 100);
    }
}

function runAnimation(alg) {
    btn.disabled = true;

    chosen_alg = alg

    const c = 0.2190422;

    count_q.style.backgroundColor = "orange";
    count_q.innerText = "Shor's Algorithm"
    count_c.style.backgroundColor = "green";
    count_c.innerText = `${chosen_alg}`;

    setTimeout(update, 500);
}


function resetAnimation() {
    
    shor = 1;
    classical = 1;
    note.innerText = "";
    count_q.innerText = "";
    count_c.innerText = "";
    count_q.style.width = 0;
    count_c.style.width = 0;
    btn.disabled = false;
}

frm.addEventListener("submit", (e) => {
    e.preventDefault();
    runAnimation(alg.value);
})