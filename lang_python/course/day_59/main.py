from flask import Flask as flask, render_template as render
import json

with open('../day59/data.json') as fil:
	DATA=json.load(fil)

# __name__ is a special attribute which is equal to the part of the program which is running.
app= flask(__name__)

# The route function is a type of python decorator.
"""	Home Page	"""
@app.route('/')	
def Home():
	return render('index.html',blogs=DATA)

"""	Post Page """
@app.route('/posts/a=<int:id>')
def Post(id):
	return render('post.html',val=DATA[id-1])

"""	About Page """
@app.route('/about')
def About():
	return render('about.html')

""" Contact Page """
@app.route('/contact')
def Contact():
	return render('contact.html')

if __name__ =='__main__':
	app.run(debug='True')