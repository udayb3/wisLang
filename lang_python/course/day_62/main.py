from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, URLField , SubmitField, TimeField, IntegerField
from wtforms.validators import DataRequired
import csv

# Initializing the object of the flask class
page = Flask( __name__ )
page.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(page)

# Creating the class and fields for the form
class CafeForm(FlaskForm):
  
  cafe = StringField( label = 'Cafe name', validators=[ DataRequired() ] )
  loc_url = URLField( label = 'URL' , validators = [ DataRequired() ] )
  time_open = StringField( label = 'Opening time' , validators = [ DataRequired() ] )
  time_close = StringField( label = 'Closing time' , validators = [ DataRequired() ] )
  rating = StringField( label = "Rating" , validators = [ DataRequired() ] )
  wifi = StringField( label = 'Wifi-Rating' , validators = [ DataRequired() ] )
  power = StringField( label = 'Power Outlets' , validators = [ DataRequired() ] )
  
  submit = SubmitField('Submit')

# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌

# Different flask routes
@page.route("/")
def home():
    return render_template("index.html")

@page.route('/Add' , methods = ['GET' , 'POST'] )
def add_cafe():
  
  form = CafeForm()
  if form.validate_on_submit():

		# Taking the information from the form and writing the information to the csv file.
    data= [ form.cafe.data , form.loc_url.data , form.time_open.data , form.time_close.data , form.rating.data , form.wifi.data , form.power.data ]
    with open( file = 'cafe-data.csv' , encoding = 'utf-8' , mode='a+' ) as fil:
      writ = csv.writer( fil , delimiter = ',' , dialect='excel')
      writ.writerow( data  )
		
    return redirect( 'Success' )
  return render_template('add.html', form=form)

@page.route('/cafes')
def cafes():
  with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
      list_of_rows.append(row)
  
  return render_template('cafes.html', DATA=list_of_rows)

        

@page.route('/Success')
def succes():
  return render_template( 'success.html' )

if __name__ == '__main__':
    page.run(debug=True)