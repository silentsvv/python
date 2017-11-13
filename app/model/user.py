from app.model import db
from flask import jsonify
from flask import Blueprint

home = Blueprint("home", __name__)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'gene_id': self.id,
            'gene_symbol': self.username,
            'p_value': self.email,
        }

# def AddOneUser():
#     user = User(
#         username='new2Ad2min',
#         email='silentsvv@126.com'
#     )
#
#     db.session.add(user)
#     db.session.commit()

@home.route('/')
def QueryAllUser():
    # return jsonify({'developers': User.query.all()})
    data = User.query.all()
    json = jsonify(eqtls=[e.serialize() for e in data])
    print(json)
    return json

    # response = serializer.get_collection(db.session, {}, 'users')
    # return jsonify(response.data)

if __name__ == "__main__":
    QueryAllUser()

