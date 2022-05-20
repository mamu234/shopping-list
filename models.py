from app import db


class User(db.Model):
   id = db.Column(db.Integer,primary_key = True)
   user = db.Column(db.String(255))
   
def __repr__(self):
 return f'User {self.username}'

class Pitches(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    user = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return f'User {self.name}'