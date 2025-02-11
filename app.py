from flask import Flask,request,redirect,render_template,url_for,session,flash
from database import db,Users
from flask_migrate import Migrate



app = Flask(__name__)

# configure database to URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:greenprod@localhost/myfreshfood'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'order_fresh_food'

db.init_app(app)

# with app.app_context():
#     db.create_all()
migrate = Migrate(app, db)



# Login functionality 
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        Username = request.form['username']
        user_password = request.form['password']

        user = Users.query.filter_by(Username=Username).first()

        if user and user.user_password == user_password:
            session['username'] = user.Username
            return redirect(url_for('home'))
        else:
            flash(' Invalid credentials')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout',methods=['GET'])
def logout():
    if 'username' in session:
        session.pop('username',None)
    return redirect(url_for('login'))

@app.route('/admin',methods=['GET','POST'])
def admin():
    return redirect(url_for('admin'))

@app.route('/profile')
def profile():
    # Only accessible if the user is logged in
    if 'username' in session:
        return render_template('profile.html', username=session['username'])
    else:
        flash('You need to log in first')
        return redirect(url_for('login'))

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        Full_name = request.form.get('Fullname')
        Username = request.form.get('Uname')

        Email = request.form.get('Email')
        PhoneNo = request.form.get('PhoneNo')
        user_password = request.form.get('Password1')
        gender = request.form.get('gender')

        useradd= Users(
            Full_name=Full_name,
            Username=Username,
            Email=Email,
            PhoneNo=PhoneNo,
            user_password=user_password,
            gender=gender
        )

        # useradd= Users(useradd)
        db.session.add(useradd)
        db.session.commit()
        flash("Account Created Successfully!!!!")
        return redirect(url_for("login"))

    else:
        return render_template('signup.html')

@app.route('/foodadd',methods=['GET','POST'])
def addfood():
    if 'username' in session:
        if request.method =='POST':
            food_name = request.form.get('name')
            Qty = request.form.get('Qty')
            Price = request.form.get('Price')

            discount = request.form.get('discount')
            Date = request.form.get('Date')
            PName = request.form.get('PName')

            result = {
                "Food_name" : food_name,
                "Food_qty": Qty,
                "Food_Price": Price,
                "Food_Discount": discount,
                "Added_date" : Date,
                "Added BY":PName
            }
            return redirect(url_for('success'))
        return render_template('foodadd.html')
    else:
        flash("Please login first")
        return redirect(url_for("login"))

@app.route('/success',methods=['GET','POST'])
def print_food():
    
    result = session.get('result', {})
    return render_template('shopfruits.html',result=result)




@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')
   



if __name__ == '__main__':
    app.run(debug =True)