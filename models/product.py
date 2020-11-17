from app import db


class Product(db.Document):
    name = db.StringField(required=True)
    description = db.StringField(required=True)
    params = db.ListField(db.DictField(), required=True)
