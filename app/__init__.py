from flask import Flask
from app.blueprints.color import bp as colorbp
from app.blueprints.fruit import bp as fruitbp

def createapp():

    app = Flask(__name__)

    app.register_blueprint(colorbp)
    app.register_blueprint(fruitbp)

    return app