from flask import render_template,redirect,url_for,request,flash
from shop.models import Seller,Admin,Product
from shop import app,db,bcrypt
from flask_login import login_user,logout_user,login_required,current_user
from shop.forms import SignUpForm,LoginForm

@app.route('/')
@login_required
def index():
   products=Product.query.filter_by(seller=current_user)
   count =0

   for i in products:
      count +=1
   return render_template('index.html',count=count)

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

@app.route('/addproduct',methods=['POST','GET'])
def add_product():
   prod_name=request.form.get('prod_name')
   cost_price=int(request.form.get('cost_price'))
   mark_up=int(request.form.get('mark_up'))
   discount=int(request.form.get('discount'))
   stock=request.form.get('stock')
   prod_type=request.form.get('prod_type')
   
   selling_price=cost_price + (cost_price * (mark_up/100))
   d=discount/100
   disc=selling_price * d
   final_price=selling_price -disc

   product=Product.query.filter_by(prod_name=prod_name).first()
   if product:
      flash("Duplicate Record Found")
      return redirect(url_for('products_page'))
   new_product=Product(
      prod_name=prod_name,
      cost_price=cost_price,
      selling_price=final_price,
      discount=disc,
      stock=stock,
      prod_type=prod_type,
      seller=current_user
   )
   try:
          
      db.session.add(new_product)
      db.session.commit()
      flash("Product Added Successfully")
      return redirect(url_for('products_page'))
   
   except:
      flash("Product not added")
      

@app.route('/all')
def all_products():
   products=Product.query.filter_by(seller=current_user).all()
   if not products:
      flash("There are no products at all.")
   return render_template('all.html',products=products)

   