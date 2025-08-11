from flask import Flask, Blueprint, request, render_template, flash, session, redirect, url_for
from models.usersModel import users
from datetime import datetime

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/register', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not users.valid_email(email):
            flash("Please enter a valid email address.", "error")
            return redirect(url_for('users.register'))
        
        re = users(username,email,password)
        check = re.register()
        
        if check:
            flash("Registered Successful!")
        else:
            flash("Not Registered")
            
    return render_template("registration.html")

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        check = users.login_method(email, password)
        row = check.login()
        
        if row:
            session['userId'] = row['id']
            session['username'] = row['username']
            flash("Successfully login")
            return redirect(url_for('tasks.tasks'))
        else:
            flash("Not login")
            return render_template("login.html")
        
    return render_template("login.html")