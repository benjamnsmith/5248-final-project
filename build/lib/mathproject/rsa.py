from flask import Blueprint, render_template, request, g
import subprocess, shlex
from hashlib import md5
from datetime import datetime
import json

bp = Blueprint('rsa', __name__, url_prefix="/rsa")

dbg = True
keysize = 256
hash = ""


@bp.route("/overview", methods=("GET", "POST"))
def rsa():
    return render_template("rsa/rsa.html")

@bp.route("/ssl", methods=("GET", "POST"))
def sslExample():
    return render_template("rsa/ssl-example.html")

@bp.route("/attack", methods=("GET", "POST"))
def rsaAttack():
    return render_template("rsa/rsa-attack.html")


# API routes
@bp.route('/keygen', methods=["POST"])
def keygen():
    global hash
    global keysize

    if not dbg:
        hash = md5(str(datetime.now()).encode()).hexdigest()
        subprocess.call(shlex.split("openssl genrsa -out keys/generated-keys/private-key-{}.pem {}".format(hash, keysize)))
        subprocess.call(shlex.split("openssl rsa -in keys/generated-keys/private-key-{}.pem  -pubout -out keys/generated-keys/public-key-{}.pem".format(hash, hash)))
        dat = subprocess.run(shlex.split("openssl rsa -in keys/generated-keys/private-key-{}.pem -noout -text".format(hash)), capture_output=True, text=True).stdout
    else:
        hash = "1e12369365ae3c9992b808d1defd80b3"
        dat = subprocess.run(shlex.split("openssl rsa -in keys/generated-keys/private-key-{}.pem -noout -text".format(hash)), capture_output=True, text=True).stdout
        
        #subprocess.call(shlex.split("openssl rsautl -encrypt -inkey keys/public-key.pem -pubin -in keys/plain.txt -out keys/{}-enc.txt".format(hash)))

    return json.dumps(fix(dat.split()), separators=(',', ':'))

@bp.route('/rsa-encrypt', methods=["POST"])
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

def genKeys():
    hash = md5(str(datetime.now()).encode()).hexdigest()
    g.hash = hash
    subprocess.call(shlex.split("openssl genrsa -out keys/generated-keys/private-key-{}.pem 256".format(hash)))
    subprocess.call(shlex.split("openssl rsa -in keys/generated-keys/private-key-{}.pem  -pubout -out keys/generated-keys/public-key-{}.pem".format(hash, hash)))
    return hash