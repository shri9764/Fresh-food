from flask import Flask, request, redirect, render_template, url_for, session, flash
from database import db, Users, Product_Details
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:greenprod@localhost/myfreshfood'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'order_fresh_food'

# Initialize the database
db.init_app(app)
migrate = Migrate(app, db)

# Login functionality
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Username = request.form['username']
        user_password = request.form['password']

        user = Users.query.filter_by(Username=Username).first()

        if user and user.user_password == user_password:
            session['username'] = user.Username
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials')
            return redirect(url_for('login'))
    return render_template('login.html')

# Logout functionality
@app.route('/logout', methods=['GET'])
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    # Only accessible if the user is logged in
    if 'username' in session:
        return render_template('profile.html', username=session['username'])
    else:
        flash('You need to log in first')
        return redirect(url_for('login'))

# Sign-up functionality
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        Full_name = request.form.get('Fullname')
        Username = request.form.get('Uname')
        Email = request.form.get('Email')
        PhoneNo = request.form.get('PhoneNo')
        user_password = request.form.get('Password1')
        gender = request.form.get('gender')

        # Create a new user and add to the database
        useradd = Users(
            Full_name=Full_name,
            Username=Username,
            Email=Email,
            PhoneNo=PhoneNo,
            user_password=user_password,
            gender=gender
        )

        db.session.add(useradd)
        db.session.commit()
        flash("Account Created Successfully!!!!")
        return redirect(url_for("login"))

    return render_template('signup.html')

# Add food item functionality
@app.route('/foodadd', methods=['GET', 'POST'])
def foodadd():
    if 'username' in session:
        if request.method == 'POST':
            Product_name = request.form.get('name')
            Qty = request.form.get('Qty')
            Price = request.form.get('Price')
            Discount = request.form.get('discount')
            Date_str = request.form.get('Date')
            Product_image = request.form.get('File')
            PName = request.form.get('PName')

            try:
                Date = datetime.strptime(Date_str, '%Y-%m-%d').date()
            except:
                flash("Invalid date format")
                return redirect(url_for('foodadd'))

            # Add the product to the database
            foods = Product_Details(
                Product_name=Product_name,
                Qty=Qty,
                Price=Price,
                Discount=Discount,
                created_Date=Date,
                Product_image=Product_image,
                PName=PName
            )

            db.session.add(foods)
            db.session.commit()
            flash("Food added Successfully!!!!")
            return redirect(url_for('foodadd'))
        return render_template('foodadd.html')
    else:
        flash("Please login first")
        return redirect(url_for("login"))

# Display fruits page
@app.route('/shopfruits', methods=['GET', 'POST'])
def Display_food():
    return render_template('shopfruits.html')

# Home route
@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
