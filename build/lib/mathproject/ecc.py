from flask import Blueprint, render_template

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