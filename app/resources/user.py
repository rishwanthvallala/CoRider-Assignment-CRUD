from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from bson import ObjectId
from bson.errors import InvalidId
from app.models.user import User
from app.schemas.user import UserSchema
from app.utils.password_utils import hash_password

user_schema = UserSchema()

class UserListResource(Resource):
    def get(self):
        users = User.objects.all()
        return user_schema.dump(users, many=True), 200

    def post(self):
        try:
            data = user_schema.load(request.json)
        except ValidationError as err:
            return {'message': 'Validation error', 'errors': err.messages}, 400

        if User.objects(email=data['email']).first():
            return {'message': 'User with this email already exists'}, 400

        data['password'] = hash_password(data['password'])
        user = User(**data).save()
        return user_schema.dump(user), 201

class UserResource(Resource):
    def get(self, user_id):
        try:
            user = User.objects(id=ObjectId(user_id)).first()
        except InvalidId:
            return {'message': 'Invalid user ID'}, 400

        if not user:
            return {'message': 'User not found'}, 404
        return user_schema.dump(user), 200

    def put(self, user_id):
        try:
            user = User.objects(id=ObjectId(user_id)).first()
        except InvalidId:
            return {'message': 'Invalid user ID'}, 400

        if not user:
            return {'message': 'User not found'}, 404

        try:
            data = user_schema.load(request.json, partial=True)
        except ValidationError as err:
            return {'message': 'Validation error', 'errors': err.messages}, 400

        if 'password' in data:
            data['password'] = hash_password(data['password'])

        user.update(**data)
        user.reload()
        return user_schema.dump(user), 200

    def delete(self, user_id):
        try:
            user = User.objects(id=ObjectId(user_id)).first()
        except InvalidId:
            return {'message': 'Invalid user ID'}, 400

        if not user:
            return {'message': 'User not found'}, 404

        user.delete()
        return '', 204