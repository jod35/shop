from flask import render_template,redirect,url_for,request,flash
from shop.models import Seller,Admin,Product
from shop import app,db,bcrypt
from flask_login import login_user,logout_user,login_required,current_user
from shop.forms import SignUpForm,LoginForm

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/products')
def products_page():
   return render_template('products.html')

@app.route('/signup',methods=['GET', 'POST'])
def sign_up():
   form=SignUpForm()
   if request.method == 'POST':
      new_seller=Seller(
         username=request.form.get('username'),
         email=request.form.get('email'),
         password=bcrypt.generate_password_hash(request.form.get('password')),
         comm_type=request.form.get('comm_type'),
      )
      try:   
          db.session.add(new_seller)
          db.session.commit()
          flash("Your account has been created! You can now login")
          return redirect(url_for('sign_up'))
      except:
          flash("Please Check your Credentials and try again!")
          return redirect(url_for('sign_up'))     

   return render_template('signup.html',form=form)

@app.route('/login',methods=['GET', 'POST'])
def login_page():
   form=LoginForm()
   email=request.form.get('email')
   password=request.form.get('password')
   user = Seller.query.filter_by(email=email).first()

   if user and bcrypt.check_password_hash(user.password,password):
      try:
         login_user(user)
         return redirect(url_for('index'))
      except :
         flash("Invalid Username or Password")
         return redirect(url_for('login_page'))
   return render_template('login.html',form=form)

@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('login_page'))