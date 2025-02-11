from flask import Flask
from flask_sqlalchemy import SQLAlchemy




db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    Username = db.Column(db.String(255), unique=True, nullable=False)
    Full_name = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), unique=True, nullable=False)
    PhoneNo = db.Column(db.String(15), unique=True, nullable=False)  # Adjusted length for phone number
    user_password = db.Column(db.String(255), nullable=False)  # Increased length for password hash
    gender = db.Column(db.String(10), nullable=True)  # Optional length for gender


    
# if __name__ == '__main__':
#     pass