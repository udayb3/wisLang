from flask import Flask as fl

# __name__ is a special attribute which is equal to the part of the program which is running.
app= fl(__name__)

# The route function is a type of python decorator.
# @app.route('/')

if __name__ =='__main__':
	app.run()