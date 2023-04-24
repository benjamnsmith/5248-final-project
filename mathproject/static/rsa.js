const s = document.getElementById("cryptex");

let s1 = String.fromCharCode(157);
let s2 = String.fromCharCode(242);

s.innerText = s1 + s2;


const encrypt_form = document.querySelector("form");
const inp_val = document.querySelector("#inp");
const res = document.querySelector("#results");

function encrypt(st) {
    let v1 = (st.charCodeAt(0)).toString(2);
    let v2 = (st.charCodeAt(1)).toString(2);

    
    if (v1.length != 8){
        v1 = "0" + v1
    }

    if (v2.length != 8){
        v2 = "0" + v2
    }

    let v = BigInt(parseInt(v1 + v2, 2));

    let e = v ** 173n;

    let c = e % 173287n;

    let b = c.toString(2);

    b1 = b.substring(0,b.length/2)
    b2 = b.substring(b.length/2,b.length)

    let c1 = String.fromCharCode(parseInt(b1,2))
    let c2 = String.fromCharCode(parseInt(b2,2))

    res.innerHTML = `<p>Let's convert "${st}" to a number we can work with:<br>`
    res.innerHTML += `${st} = ${st.charCodeAt(0)} ${st.charCodeAt(1)} = ${v1} ${v2} = ${v}<br>`
    res.innerHTML += `\$c \\equiv ${v}^{173} \\equiv ${c} \\pmod{85988}\$</br>`
    res.innerHTML += `${c} = ${b1} ${b2} = ${parseInt(b1,2)} ${parseInt(b2,2)} = "${c1}${c2}" </br>`
    res.innerHTML += `So, "${st}" encrypted with the RSA key (85988,173) is "${c1}${c2}"`

    MathJax.typeset()
}

encrypt_form.addEventListener("submit", (e) => {
    e.preventDefault();

    const txtbox = document.querySelector("#plaintext");

    var txt = txtbox.value.substring(0,2);

    txt = encrypt(txt);
})