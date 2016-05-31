from flask import Flask  
from flask_sqlalchemy import SQLAlchemy  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:marystl@localhost/pythonspot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Register(db.Model):

	__tablename__ = 'Register'
	id = db.Column(db.Integer , primary_key = True)
	username = db.Column(db.String(20) , unique = True)
	firstname = db.Column(db.String(30))

	def __init__(self,username,firstname):
		self.username = username
		self.firstname = firstname

	
