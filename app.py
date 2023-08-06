import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from models import *
from sqlalchemy import func

# Path: app.py
basedir = os.path.abspath(os.path.dirname(__file__))

# Path: app.py
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'dcdata.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'beyond_course_scope'
db.init_app(app)


# Manage log in sessions
login_manager = LoginManager()
login_manager.login_view = 'LogIn' # default login route
login_manager.init_app(app)


@login_manager.user_loader
def load_user(account_id):
    return Credentials.query.get(account_id)

@app.route('/')
def landingPage():
    return render_template('landingPage.html')


@app.route('/home')
def homePage():
    return render_template('homePage.html')


@app.route('/about')
def aboutPage():
    return render_template('aboutPage.html')


@app.route('/newCalculation')
def newCalculation():
    return render_template('newCalculation.html')

@app.route('/login', methods = ['GET', 'POST'])
def logIn():
    default_route_function = 'homePage'
    default_user_route_function = 'homePage'

    if request.method == 'GET':
        # Determine where to redirect user if they are already logged in
        if current_user and current_user.is_authenticated:
            if current_user.role in ['EMPLOYEE', 'ADMIN']:
                return redirect(url_for(default_route_function))
            elif current_user.role == 'PUBLIC':
                return redirect(url_for(default_user_route_function, user_id=0))
        else:
            redirect_route = request.args.get('next')
            return render_template('logIn.html', redirect_route=redirect_route)

    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        redirect_route = request.form.get('redirect_route')

        user = Credentials.query.filter_by(username=username).first()

        # Validate user credentials and redirect them to initial destination
        if user and check_password_hash(user.password, password):
            login_user(user)

            if current_user.role in ['EMPLOYEE', 'ADMIN']:
                return redirect(redirect_route if redirect_route else url_for(default_route_function))
            elif current_user.role == 'PUBLIC':
                return redirect(redirect_route if redirect_route else url_for(default_user_route_function, user_id=0))
        else:
            flash(f'Your login information was not correct. Please try again.', 'error')

        return redirect(url_for('LogIn'))

    return redirect(url_for('LogIn'))

# route for sign up page
@app.route('/signup', methods=['GET', 'POST'])
def signUp():
    if request.method == 'GET':
        return render_template('signUp.html', action='create')

    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        # set variable for the password
        sha_password = generate_password_hash(password, method='sha256', salt_length=8)

        user = Credentials(username=username, password=sha_password, first_name=first_name, last_name=last_name,
                          email=email)
        # add to database and log the user in
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f'{username} was successfully added!', 'success')
        return redirect(url_for('homePage'))

# log out route
@app.route('/logout')
@login_required
def logout():
    # if cart exists delete it upon log out
    if 'cart' in session:
        del (session['cart'])
    # sign the user out
    logout_user()
    flash(f'You have been logged out.', category='success')
    return redirect(url_for('homePage'))


if __name__ == '__main__':
    app.run(debug=True)