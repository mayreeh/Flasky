from flask import Flask  , render_template , request
from form import RegisterForm
from flask_bootstrap import Bootstrap
from model import Register
from app import db


app = Flask(__name__)
app.secret_key = 's3cr3t'
Bootstrap(app)

@app.route('/' , methods = ['GET' , 'POST'])
def home():
	form = RegisterForm()
	if request.method == 'POST':
		username = request.form['username']
		firstname = request.form['firstname']
		register = Register(username , firstname)
		db.create_all()
		db.session.add(reg)
		db.session.commit()
		return "success"
	else:
		return render_template('register.html' , form = form)
	


@app.route('/test')
def test():
	return render_template('test.html')



if __name__ == '__main__':
	app.run(debug = True)

