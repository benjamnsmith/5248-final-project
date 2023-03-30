from flask import (
    Flask, render_template, g, request, url_for
)

import subprocess, shlex
from hashlib import md5
import json
from datetime import datetime

strings = ["The proof is trivial and left as an exercise to the reader"]

dbg = True

app = Flask(__name__)

hash= ""
keysize = 1024

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/rsa", methods=("GET", "POST"))
def rsa():
    return render_template("rsa.html")

@app.route("/rsa-ssl", methods=("GET", "POST"))
def sslExample():
    return render_template("ssl-example.html")

@app.route("/rsa-attack", methods=("GET", "POST"))
def rsaAttack():
    return render_template("rsa-attack.html")


def genKeys():
    hash = md5(str(datetime.now()).encode()).hexdigest()
    g.hash = hash
    subprocess.call(shlex.split("openssl genrsa -out keys/generated-keys/private-key-{}.pem 256".format(hash)))
    subprocess.call(shlex.split("openssl rsa -in keys/generated-keys/private-key-{}.pem  -pubout -out keys/generated-keys/public-key-{}.pem".format(hash, hash)))
    return hash

def fix(lst):
    terms = ["Private-Key", "modulus", "publicExponent", "privateExponent", "prime1", "prime2", "exponent1", "exponent2", "coefficient"]
    curTerm = ""
    dic = {}
    for elem in lst:
        elem = elem.replace(":", "")
        if elem in terms:
            curTerm = elem
        else:
            try:
                dic[curTerm] += elem
            except:
                dic[curTerm] = elem
    return dic

@app.route('/keygen', methods=["POST"])
def keygen():
    global hash
    global keysize
    if not dbg:
        hash = md5(str(datetime.now()).encode()).hexdigest()
        subprocess.call(shlex.split("openssl genrsa -out keys/generated-keys/private-key-{}.pem {}".format(hash, keysize)))
        subprocess.call(shlex.split("openssl rsa -in keys/generated-keys/private-key-{}.pem  -pubout -out keys/generated-keys/public-key-{}.pem".format(hash, hash)))
        dat = subprocess.run(shlex.split("openssl rsa -in keys/generated-keys/private-key-{}.pem -noout -text".format(hash)), capture_output=True, text=True).stdout
        d = fix(dat.split())
    else:
        hash = "0d4488205e2d9ab0eee4a1100d34d4e1"
        dat = subprocess.run(shlex.split("openssl rsa -in keys/generated-keys/private-key-{}.pem -noout -text".format(hash)), capture_output=True, text=True).stdout
        
        subprocess.call(shlex.split("openssl rsautl -encrypt -inkey keys/public-key.pem -pubin -in keys/plain.txt -out keys/{}-enc.txt".format(hash, strings[0], hash)))

        d = fix(dat.split())

    return json.dumps(d, separators=(',', ':'))


@app.route('/rsa-encrypt', methods=["POST"])
def rsaEncrypt():
    global hash
    if not dbg:
        pass
    else:
        txt = request.form["plaintext"]
        with open("{}-plain.txt".format(hash), "w") as fil:
            fil.write(txt)
            fil.close()
        
        dat = subprocess.run(shlex.split("openssl rsautl -encrypt -inkey public-key-{}.pem -pubin -in {}-plain.txt -out {}-enc.txt".format(hash, hash, hash)), capture_output=True, text=True).stdout
    return 
    
@app.route('/reading')
def reading():
    return render_template("reading.html")


if __name__ == "__main__":
    app.run(port=7777)