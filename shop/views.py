from flask import render_template,redirect,url_for,request,flash
from shop.models import Seller,Admin,Product
from shop import app,db,bcrypt
from shop.forms import SignUpForm

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

@app.route('/login')
def login_page():
   return render_template('login.html')