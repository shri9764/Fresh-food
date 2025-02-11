from database import food_table,Users,db , init_db
from flask import Flask, render_template, request, redirect, url_for,flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import migrate, Migrate
from flask_login import fresh_login_required
from flask_login import user_logged_in ,UserMixin, login_user,login_required,LoginManager, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/freshfood_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.secret_key = 'Personal-shri-Jagtap-TCS'
# db = SQLAlchemy(app)

init_db(app)





@app.route('/login', methods=['GET', 'POST'])
def login():


    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        
        user = Users.query.filter_by(Username = username).first()
        if user and user.check_password(password): 
            # session['username'] = username
            login_user(user) 
            flash('Login successful!', 'success') 
            return redirect(url_for('/login'))
    
    return render_template ('login.html')



@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        Fullname = request.form.get('Fullname') 
        Uname = request.form.get('Uname') 
        PhoneNo = request.form.get('PhoneNo')
        Email = request.form.get('Email')
        Password = request.form.get('Password')
        Password1 = request.form.get('Password1')
        gender = request.form.get('gender')

        # if len(PhoneNo) <= 12 :
        #     flash( " Please enter 10 digit mobile number  ")
        #     return redirect(url_for('signup')) 
        
        if Password != Password1:
            flash( " Both password not the same...   ")
            return redirect(url_for('signup')) 
        

        Status = 1

        insert = Users(Full_name =Fullname , Username = Uname , Email = Email , Mob_No = PhoneNo , Password = bcrypt.hashpw(Password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') , Gender = gender  ,Status = Status)

        db.session.add(insert)
        db.session.commit()
        flash(f'Form submitted successfully! Welcome {Fullname} ')
        return redirect(url_for('login'))

    return render_template ('signup.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     return render_template ('login.html')




@app.route("/foodadd", methods =['GET', 'POST'])
def foodadd():

    # Add food in DB
    if request.method == 'POST':
        name = request.form.get('name')
        qty   = request.form.get('Qty')
        price = request.form.get('Price')
        discount = request.form.get('discount')
        File = request.files.get('File')
        date = request.form.get('date')
        PName = request.form.get('PName')

        if not date:
            date = datetime.today().strftime('%d-%m-%y')
        if not name:
            pass

        Qty = int(qty)
        Price = int(price)
        Discount = int(discount)



        entry = food_table( Qty = Qty, Food_name = name, F_image =File ,Price = Price,Discount = discount , Date = date, PName = PName )
        db.session.add(entry)
        db.session.commit()
        #flash("<h6> Food added Successfully <h6>")
        return redirect(url_for('foodadd'))
    return render_template ('foodadd.html')


@app.route("/about")
def about():
    return render_template ('about.html')



@app.route("/shopfruits")
def shopfruits():
    return render_template ('shopfruits.html')


@app.route('/drinks') 
def drinks():
    user= 'Krishna'
    return render_template ('drinks.html')


@app.route('/home')
@app.route('/s')
def home():


    return render_template ('index.html', user = current_user)



if __name__ == "__main__":

    app.run(debug=True)
    #app.run()