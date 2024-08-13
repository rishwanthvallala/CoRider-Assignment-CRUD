from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt

from config.config import Config

db = MongoEngine()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)

    api = Api(app)

    from app.resources.user import UserResource, UserListResource
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<string:user_id>')

    return app