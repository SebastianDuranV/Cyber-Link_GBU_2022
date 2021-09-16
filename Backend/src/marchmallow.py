from flask_marshmallow import Marshmallow
from sql import app

ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'names', 'lastname', 'details', 'approved')

user_schema = UserSchema()
user_schemas = UserSchema(many=True)

