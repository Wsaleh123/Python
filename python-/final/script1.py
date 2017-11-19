from flask import Flask, render_template, request, send_file
from flask.ext.sqlalchemy import SQLAlchemy
from email.mime.text import MIMEText
import smtplib
from sqlalchemy.sql import func
from werkzeug import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'
db = SQLAlchemy(app)

class Data(db.Model):
	__tablename__="data"
	id = db.Column(db.Integer, primary_key = True)
	email_ = db.Column(db.String(120))
	height_ = db.Column(db.Integer)

	def __init__(self, email_, height_):
		self.email_ = email_
		self.height_ = height_

def send_email(email, height, average_height, count):
		from_email = "real.microsoftinc@gmail.com"
		from_password = "wesam098"
		to_email=email

		subject = "Height Data"
		message = "Hey there, your height is <strong>%s</strong>cm. Average height of all is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people." %(height, average_height, count)

		msg=MIMEText(message, 'html')
		msg['Subject']=subject
		msg['To']=to_email
		msg['From'] = from_email

		gmail= smtplib.SMTP('smtp.gmail.com', 587)
		gmail.ehlo()
		gmail.starttls()
		gmail.login(from_email, from_password)
		gmail.send_message(msg)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
	if request.method=='POST':
		file = request.files["file"]
		file.save(secure_filename("uploaded" + file.filename))
		with open("uploaded" + file.filename, "a") as f:
			f.write("This was added later")
		print(file)
		print(type(file))
		return render_template("index.html", btn="download.html")
		return render_template("success.html")
		return render_template("index.html",
		text="Seems like we've got something from that email address already")


@app.route("/download")
def download():	
	if request.method=='POST':
		file = request.files["file"]
		file.save(secure_filename("uploaded" + file.filename))
		with open("uploaded" + file.filename, "a") as f:
			f.write("This was added later")
		print(file)
		print(type(file))
		return render_template("index.html", btn="download.html")
		return render_template("success.html")
		return render_template("index.html",
		text="Seems like we've got something from that email address already")
	return send_file("uploaded" + file.filename, attachment_filename="yourfile.csv", as_attachment=True)
	

if __name__ == '__main__':
	app.debug = True
	app.run()
