from flask import Flask
from waitress import serve

def create_app():

    app = Flask(__name__)

    import ecc, pages, rsa
    app.register_blueprint(ecc.bp)
    app.register_blueprint(pages.bp)
    app.register_blueprint(rsa.bp)

    
    return app

app = create_app()

serve(app, port=5000)
