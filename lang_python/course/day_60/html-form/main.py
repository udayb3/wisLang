from flask import Flask as flask, render_template as render
from flask import request
# __name__ is a special attribute which is equal to the part of the program which is running.
app= flask(__name__)

# The route function is a type of python decorator.
@app.route('/')
def form():
	return render('index.html')

@app.route('/login', methods=['POST','GET'])
def receive_data():
	name=request.form["username"];	password=request.form["password"]
	return render('login.html',name=name, password=password)

if __name__ =='__main__':
	app.run(debug='True')