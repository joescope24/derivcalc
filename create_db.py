from app import app, db
from models import Credentials, Calculations, Contact
from werkzeug.security import generate_password_hash

with app.app_context():
    db.drop_all()
    db.create_all()

    # Initial loading of users
    users = [
        {'username': 'public', 'password': generate_password_hash('publicpw', method='sha256'),
         'first_name':'Public', 'last_name':'Test', 'email': 'public@umd.edu', 'role':'PUBLIC'},
        {'username': 'employee', 'password': generate_password_hash('employeepw', method='sha256'),
         'first_name': 'Employee', 'last_name': 'Employee', 'email': 'employee@umd.edu', 'role': 'EMPLOYEE'},
        {'username': 'admin', 'password': generate_password_hash('adminpw', method='sha256'),
         'first_name': 'Admin', 'last_name': 'Admin', 'email': 'admin@umd.edu', 'role': 'ADMIN'},
    ]

    # add users to databse
    for each_user in users:
        print(f'{each_user["username"]} inserted into user')
        a_user = Credentials(username=each_user["username"], password=each_user["password"], first_name=each_user["first_name"],
                             last_name=each_user["last_name"], email=each_user["email"], role=each_user["role"])
        db.session.add(a_user)
        db.session.commit()
