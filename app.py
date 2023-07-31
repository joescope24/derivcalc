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


if __name__ == '__main__':
    app.run(debug=True)