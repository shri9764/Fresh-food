from flask import Flask, render_template, request, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import migrate, Migrate
from flask_login import user_logged_in ,UserMixin, login_user,login_required,LoginManager, logout_user, current_user
import bcrypt

#**************** Add Secret key *************


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/freshfood_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db = SQLAlchemy(app)

def init_db(app):
    
    db.init_app(app)

migrate = Migrate(app, db)
    
# flask login user setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# class user(db.Model):
#     pass




class food_table(db.Model):
    Sr_No = db.Column(db.Integer, primary_key=True)  
    Food_name = db.Column(db.String(80),unique = True, nullable=False) 
    Qty = db.Column(db.Integer, nullable=False)  
    F_image = db.Column(db.String(120), nullable=True)  
    Price = db.Column(db.Float, nullable=False) 
    Discount = db.Column(db.Float, nullable=False) 
    Date = db.Column(db.Date) 
    PName = db.Column(db.String(120), nullable=False)  

   
    print("Food table Created successfully!!!!!")


class Users(db.Model):
    id =  db.Column(db.Integer,primary_key = True, nullable = False)
    Full_name = db.Column(db.String(20), unique = False, nullable = False)
    Username = db.Column(db.String(20), unique = True, nullable = False)
    Email = db.Column(db.String(20), unique = True, nullable = False)
    Mob_No =  db.Column(db.String(20),unique = True, nullable = False)
    Password = db.Column(db.String(20), nullable = False)
    Gender = db.Column(db.String(20),nullable = False)
    Status = db.Column(db.String(20),nullable = False)

    
    def __init__(self, Full_name, Username,Password, Email,Mob_No,Gender,Status):

        self.id = id
        self.Full_name = Full_name
        self.Username = Username
        self.Email = Email
        self.Mob_No = Mob_No
        self.Password = bcrypt.hashpw(Password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.Gender = Gender
        self.Status = Status
    
    def check_password(self,Password):
        return self.Password   


# Initialize the database (only needed once)
with app.app_context():
    db.create_all()
    



if __name__ == '__main__':
    pass