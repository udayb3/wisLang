from flask import Flask, render_template as render, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TimeField, DateTimeField, SubmitField, EmailField
from wtforms.validators import DataRequired as req

# Setting up the flask application
page=Flask(__name__)

# setting up the password for the csrf protection in flask application
page.secret_key=""

# Setting up the class for wtforms
class myform(FlaskForm):
  username = StringField(label= 'Name',validators=[req()])
  mail = EmailField(label= 'E-mail',validators=[req()])
  password = PasswordField(label='Password',validators=[req()])
  
  submit = SubmitField(label = "Submit")
  
# Routing the user to the starting page 
@page.route('/')
def intro():
	return render('index.html')

@page.route('/Login', methods=['POST','GET'])
def login():
  form = myform()
  
  T_mail = form.mail.data
  T_password= form.password.data
  
  database = [ ( "aman@gmail.com" , "ver234" )  ]
  
  if request.method == 'POST':
    
    if form.validate_on_submit() and ( T_mail , T_password ) in database:
      return redirect("/Success")
    else:
      return redirect("/Denied")
  
  return render('login.html', form=form)

@page.route( '/Success' )
def success():
  return render('success.html')

@page.route('/Denied')
def denied():
  return render('denied.html')

if (__name__=='__main__'):
	page.run(debug=True)
