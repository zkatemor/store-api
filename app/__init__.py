from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine

db = MongoEngine()
api = Api()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    api.app = app
    return app
