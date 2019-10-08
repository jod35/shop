from flask import render_template,redirect,url_for
from shop import app,db


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/products')
def products_page():
   return render_template('products.html')

@app.route('/signup')
def sign_up():
   return render_template('signup.html')

@app.route('/login')
def login_page():
   return render_template('login.html')