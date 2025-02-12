from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    Username = db.Column(db.String(255), unique=True, nullable=False)
    Full_name = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), unique=True, nullable=False)
    PhoneNo = db.Column(db.String(15), unique=True, nullable=False)
    user_password = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(10), nullable=True)

class Product_Details(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    Product_name = db.Column(db.String(255), unique=True, nullable=False)
    Price = db.Column(db.String(255), nullable=False)
    Qty = db.Column(db.String(255), nullable=False)
    Discount = db.Column(db.String(15), nullable=False)
    Disc_price = db.Column(db.String(255), default='0', nullable=False)
    Product_image = db.Column(db.String(255), nullable=True)
    created_Date = db.Column(db.Date, nullable=True)
    PName = db.Column(db.String(255), nullable=False)




# If you need to initialize the app and the database, you can use the following code:
# if __name__ == '__main__':
#     app.run(debug=True)
