from flask import Blueprint, render_template



bp = Blueprint('pages', __name__)

# page routes
@bp.route("/")
def index():
    return render_template("index.html")

@bp.route('/reading')
def reading():
    return render_template("reading.html")


