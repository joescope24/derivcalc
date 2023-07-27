from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()

# create user table
class Credentials(UserMixin, db.Model):
    __tablename__ = "Credentials"

    username = db.Column(db.String(40), primarykey=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(10), nullable=False)

# initialize credentials table
    def __init__(self, username, password, first_name, last_name, email, role='PUBLIC'):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role = role

# get id
    def get_id(self):
        return (self.username)

    def __repr__(self):
       return f"({self.username}){self.password}{self.role}"
# create requests table
class Calculations(db.Model):
   __tablename__ = "Calculations"

   calc_id = db.Column(db.Integer, primary_key=True)
   account_id = db.Column(db.Integer, db.ForeignKey('Credentials.username'), nullable=False)
   type = db.Column(db.String(30), nullable=False)
   callBinom = db.Column(db.Binomial, nullable=False)
   strike = db.Column(db.Integer, nullable=False)
   maturity = db.Column(db.Integer, nullable=False)
   paths = db.Column(db.Integer, nullable=False)
   divisions = db.Column(db.Integer, nullable=False)
   interestRate = db.Column(db.Float, nullable=False)
   initialStockPrice = db.Column(db.Float, nullable=False)
   finalPrice = db.Column(db.Integer, nullable=False)

# initialize requests table
   def __init__(self, account_id, type, callBinom, strike, maturity, paths, divisions, interestRate, initialStockPrice, finalPrice):
       self.account_id = account_id
       self.type = type
       self.callBinom = callBinom
       self.strike = strike
       self.maturity = maturity
       self.paths = paths
       self.divisions = divisions
       self.interestRate = interestRate
       self.initialStockPrice = initialStockPrice
       self.finalPrice = finalPrice

   def __repr__(self):
       return f"{self.type}"

