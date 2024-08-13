from app import db

class User(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)

    def __repr__(self):
        return f'<User {self.email}>'