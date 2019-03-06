from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
# from . import login_manager
# from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key=True)
    firstName= db.Column(db.String(255),index = True)
    lastName= db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True , index=True)
    bio= db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure=db.Column(db.String(255))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    address_id=db.Column(db.Integer,db.ForeignKey('addresses.id'))
    contact_id=db.Column(db.Integer,db.ForeignKey('contacts.id'))
    products= db.relationship('Product',backref='user' ,lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Product(db.Model):
     __tablename__= 'products'

     id = db.Column(db.Integer,primary_key=True)
     name= db.Column(db.String(255),index = True)  
     description= db.Column(db.String(255)) 
     price =db.Column(db.Integer)
     contact_id=db.Column(db.Integer,db.ForeignKey('contacts.id'))
     location_id=db.Column(db.Integer,db.ForeignKey('locations.id'))
     user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
     transaction_id=db.Column(db.Integer,db.ForeignKey('transactions.id'))
     cart_id=db.Column(db.Integer,db.ForeignKey('carts.id'))



class Contact(db.Model):
      __tablename__ ='contacts'
      id = db.Column(db.Integer,primary_key=True)
      firstName= db.Column(db.String(255),index = True)
      lastName= db.Column(db.String(255),index = True)
      phone_number= db.Column(db.Integer)
      email=db.Column(db.String(255),index = True)
      products = db.relationship('Product',backref='contact' ,lazy='dynamic')
      users = db.relationship('User',backref='contacte' ,lazy='dynamic')

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'   

class Transaction(db.Model):
     __tablename__ ='transactions'
     id = db.Column(db.Integer,primary_key = True)
     seller=db.Column(db.String(255))
     buyer=db.Column(db.String(255))
     products = db.relationship('Product',backref='transaction' ,lazy='dynamic')
     total_price=db.Column(db.Integer)
      


class Cart(db.Model):
      
      __tablename__= 'carts'
      id = db.Column(db.Integer,primary_key = True)
      products = db.relationship('Product',backref='cart' ,lazy='dynamic')

   

     




