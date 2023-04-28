from flask import Blueprint, render_template, request

from tinyec import registry
import secrets, json

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
def pollard():
    pass
    