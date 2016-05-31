from flask_wtf import Form
from wtforms import StringField , TextField , IntegerField , validators


class RegisterForm(Form):

	username = StringField('username' , [validators.required()])
	firstname = StringField('First Name' , [validators.required()])


	


