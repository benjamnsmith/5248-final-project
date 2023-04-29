from flask import Blueprint, render_template, request

from tinyec import registry
import secrets, json, math, subprocess, shlex

bp = Blueprint('ecc', __name__, url_prefix="/ecc")


@bp.route("/overview")
def ecc():
    return render_template("ecc/ecc.html")

@bp.route("/diffie-hellman")
def eccdh():
    return render_template("ecc/ecc-dh.html")

@bp.route("/attack")
def eccAttack():
    return render_template("ecc/ecc-attack.html")



def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

# api endpoints
@bp.route('/ecdh-keys', methods=["POST"])
def ecdhKeys():
    curve = registry.get_curve('brainpoolP256r1')
    keys = {}

    alicePrivKey = secrets.randbelow(curve.field.n)
    keys['alice_priv'] = hex(alicePrivKey)

    alicePubKey = alicePrivKey * curve.g
    keys['alice_pub'] = compress(alicePubKey)


    bobPrivKey = secrets.randbelow(curve.field.n)
    keys['bob_priv'] = hex(bobPrivKey)

    bobPubKey = bobPrivKey * curve.g
    keys['bob_pub'] = compress(bobPubKey)

    aliceSharedKey = alicePrivKey * bobPubKey
    bobSharedKey = bobPrivKey * alicePubKey
    if aliceSharedKey == bobSharedKey:
        keys['shared'] = compress(aliceSharedKey)

    dat = json.dumps(keys)
    return dat

@bp.route('/pollard', methods=['POST'])
def pollard_api():
    
    n = int(request.form['n'])
    try:
        g = pollard(n)
        info = {}
        global runs
        info['runs'] = runs
        info['got'] = g
        info['b'] = triedB
        return json.dumps(info)
    except: 
        return -1
    
    


nextB = 5
triedB = []
runs = 0


def primes(n):
    sieve = [True] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i, n + 1, i):
                sieve[j] = False
    return primes


def pollard(n):
    global runs
    global triedB
    global nextB

    runs += 1
    B = nextB
    triedB.append(B)
    prime_list = primes(B)
    M = 1
    for q in prime_list:
        exponent = math.floor(math.log(B, q))
        M *= (q ** exponent)
    a = 2

    try:
        g = int(subprocess.run(shlex.split("wolframscript -c 'GCD[{}^{} - 1, {}]'".format(a, M, n)), capture_output=True, text=True).stdout)

    except:
        raise Exception('not enough memory')
    if 1 < g < n:
        return g
    elif g == 1:
        nextB = B+2
    elif g == n:
        nextB = B-1

    if nextB < 0 or nextB > n or nextB in triedB:
        return -1
    else:
        return pollard(n)
