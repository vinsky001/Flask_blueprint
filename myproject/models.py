from extensions import db
#Let's create database table
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    #Username to have a maximum of 20 characters
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(100), unique=True)
    brand = db.Column(db.String(20), nullable=False, unique=True)
    #password to have a max of 80 characters
    password = db.Column(db.String(80), nullable=False)