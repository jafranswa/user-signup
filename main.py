from flask import Flask, request, redirect, render_template
import os
import jinja2

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/")
def index():
    return render_template('login.html')


@app.route('/add_user', methods =['POST'])
def validate_user_name():
    new_user = request.form['new-user']
    user_name_error = ''
    password = request.form['password']
    password_error = ''
    confirm_password = request.form['confirm-password']
    passmatch_error = ''
    email = request.form['email']
    email_error = ''
    if new_user == '':
        user_name_error = 'please enter a user name'
        return render_template('login.html', user_name_error=user_name_error)
    elif len(password) <= 3:
        password_error = 'password is to short'
        return render_template('login.html', password_error = password_error)
    elif password != confirm_password:
        passmatch_error = 'passwords do not match'
        return render_template('login.html', user_name_error= user_name_error, password_error=password_error, passmatch_error = passmatch_error, email_error= email_error)
    elif email == '':
        return '<h1> Welcome, '+new_user+'</h1>'
    elif '@' not in email or '.' not in email or len(email) < 4 or len(email) > 20 or ' ' in email:    
        email_error = 'Please enter a valid email' #a single @, a single ., contains no spaces, and is between 3 and 20 characters
        return render_template('login.html', user_name_error= user_name_error, password_error=password_error, passmatch_error = passmatch_error, email_error= email_error)
    else:
        return '<h1> Welcome, '+new_user+'</h1>'



#def validate_confirm_password():
#    confirm_password = request.form['confirm-password']
#    password_confirm_error = ''

#def validate_email():
#    email = request.form['email']
#    email_error = ''


app.run()