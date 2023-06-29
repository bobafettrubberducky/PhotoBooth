from flask import request, render_template, redirect, flash, session
from flask_app import app

from flask_app.models.user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#! Dashboard Page - GET
@app.route('/', methods=['GET'])
def root():
    return render_template("dashboard.html")

#! CREATE USER - GET
@app.route('/register', methods=['GET'])
def create_user():
    return render_template('new_user.html')

#! CREATE USER - POST (action is Create New User in /register)
@app.route('/register', methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/register')
    
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "user_name": request.form["user_name"],
        "password": bcrypt.generate_password_hash(request.form["password"]), #! Hash the password created by the user
        "profile_pic": request.form.get("profile_pic", ""), #! use get method  if nothing in profile_pic then set default e value empty string ""
    }

    id = User.save(data)
    # id = 1

    session["user_id"] = id
    # session={"user_id":1}
    
    return redirect("/login")


#! Login Page GET
@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")

# Login Page POST
@app.route('/login', methods=['POST'])
def login_verify():

    data = { "email":request.form["email"] }
    
    user = User.get_by_email(data)

    if not user:
        flash("Invalid Email/Password")
        return redirect("/login")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect("/login")
    
    session['user_id'] = user.id
    session['user_name'] = user.user_name

    return redirect("/set-profile-pic")

#/logout - if user_id no in session then session.clear
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/')


