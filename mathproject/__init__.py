from flask import Flask


def create_app():

    app = Flask(__name__)

    from . import ecc, pages, rsa
    app.register_blueprint(ecc.bp)
    app.register_blueprint(pages.bp)
    app.register_blueprint(rsa.bp)

    
    return app
