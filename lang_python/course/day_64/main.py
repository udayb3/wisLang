from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,  String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

# Creating the base class which will be later used for making a table which will be already defined
class Base( DeclarativeBase ):
  pass

# Creating the flask app and linking it with the database
page = Flask(__name__)
page.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# Creating the SQLite database
db = SQLAlchemy( model_class= Base )

# Configuring the key and the bootstrap for the flask
page.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(page)

# Initialising the flask page
db.init_app(page)

# Initialising the 3 tables according to the requirements 
class Books( db.Model ):
  id: Mapped[int] = mapped_column( Integer , primary_key=True )
  Title: Mapped[str] = mapped_column( String , nullable=False , unique=True )
  Year: Mapped[int] = mapped_column( String , nullable=False)
  Creator: Mapped[str] = mapped_column( String , unique=False , nullable=False )
  Rating: Mapped[float] = mapped_column( Float , nullable=False )
  One_liner : Mapped[str] = mapped_column( String  )
  Description : Mapped[str] = mapped_column( String , nullable=False )
  url : Mapped[str] = mapped_column( String , nullable=False )

class Movies( db.Model ):
 
  id: Mapped[int] = mapped_column( Integer , primary_key=True )
  Title: Mapped[str] = mapped_column( String , nullable=False , unique=True )
  Year: Mapped[int] = mapped_column( String , nullable=False)
  Creator: Mapped[str] = mapped_column( String , unique=False , nullable=False )
  Rating: Mapped[float] = mapped_column( Float , nullable=False )
  One_liner : Mapped[str] = mapped_column( String  )
  Description : Mapped[str] = mapped_column( String , nullable=False )
  url : Mapped[str] = mapped_column( String , nullable=False )
 
class Anime( db.Model ):
 
  id: Mapped[int] = mapped_column( Integer , primary_key=True )
  Title: Mapped[str] = mapped_column( String , nullable=False , unique=True )
  Year: Mapped[int] = mapped_column( String , nullable=False)
  Creator: Mapped[str] = mapped_column( String , unique=False , nullable=False )
  Rating: Mapped[float] = mapped_column( Float , nullable=False )
  One_liner : Mapped[str] = mapped_column( String  )
  Description : Mapped[str] = mapped_column( String , nullable=False )
  url : Mapped[str] = mapped_column( String , nullable=False )

# Creating the tables
with page.app_context():
  db.create_all()

# Creating a dictionary to link all the 3 options to one page
Topics = {
  ('Movies' , 'One' ) : ( 'See the top ten movies ' ,  'For the complete list, go ' ), ( 'Anime' , 'Two' ) : ( 'See the top ten anime series ' ,  'For the complete list, go ' ) , ( 'Books' , 'Three') : ( 'See the top ten Books ' ,  'For the complete list, go ' ) 
}
con = {
  'Books':Books ,  'Movies':Movies , 'Anime':Anime ,
}

@page.route("/" , methods=["GET"])
def index():
    return render_template("index.html" , items = Topics )

@page.route("/Home" , methods=["GET"])
def home():
  
    db_name = request.args.get('DB' )   
    coun=0
    
    result = db.session.execute( db.select( con[db_name] ).order_by((10 - con[db_name].Rating) ).where(con[db_name].id<=10) )
    rows = result.scalars()
    
    return render_template( "home.html" , DB=db_name , data = rows )

@page.route("/Add" , methods=['POST' , 'GET'])
def add():
  db_name = request.args.get('DB')
  ques={
    'Movies':['Name of the movie' , 'Release year of the movie' , 'Favourite character from the movie' , 'Rating' , 'One-liner for the movie' , 'Description' , 'URL for movie poster'] ,
    'Anime':['Name of the anime/manga series' , 'Release year of the anime/manga' , 'Author of the series' , 'Rating' , 'One-liner for the series' , 'Description' , 'URL for series poster'] ,
    'Books':['Name of the book' , 'Release year of the book' , 'Author of the book' , 'Rating' , 'One-liner for the book' , 'Description' , 'URL for book cover'] ,
  }
  
  if( request.method=="POST" ):
    temp = con[db_name](
      Title = request.form.get( key = "title" ),
      Year = request.form.get( key = "year" ),
      Creator = request.form.get( key = "creator" ),
      Rating = request.form.get( key = "rating" ),
      One_liner = request.form.get( key = "one_liner" ),
      Description = request.form.get( key = "description" ),
      url = request.form.get( key = "url" )
    )
    db.session.add( temp )
    db.session.commit()
    
    return redirect( url_for( 'home' , id=db_name ) )
  
  return render_template('add.html' , DB=db_name , Question=ques[db_name])

@page.route("/Delete")
def delete():
  
  db_name = request.args.get( key = 'name' )
  id = request.args.get( key = 'id' )
  item_del = db.session.execute( db.select( con[db_name] ).where( con[db_name].id == id ) ).scalar()
  
  # Deleting the entry for the book whose id we have been given
  db.session.delete( item_del )
  db.session.commit()
  
  return redirect( url_for( 'home' , id=db_name) )

@page.route( "/Update" , methods=['POST','GET'])
def update():
  db_name = request.args.get( key = 'name' )
  id = request.args.get( key='id' )
  
  item_upd = db.session.execute( db.select( con[db_name] ).where( con[db_name].id == id ) ).scalar()
  
  if(request.method == 'POST'):
    
    # Updating the values of the database row
    item_upd.Rating = request.form[ 'rating' ]
    temp = request.form['review']
    url_temp = request.form['url']
    
    if( len(temp) > 0):
      item_upd.One_liner = temp
      
    if( len(url_temp) > 0 ):
      item_upd.url = url_temp
    
    # Commiting the updates to the database
    db.session.commit()
    
    return redirect( url_for('home' , DB = db_name) )
  
  return render_template( 'edit.html' , DB = db_name , name = item_upd.Title, prat = item_upd.Rating)


@page.route( "/Select" , methods =[ 'GET' ] )
def show():
  db_name = request.args.get( key='DB' )
  
  result = db.session.execute( db.select( con[db_name] ).order_by( con[db_name].Rating ).where(con[db_name].id<=10) )
  rows = result.scalars()
    
    
  return render_template('show.html' , DB = db_name , data = rows )



if __name__ == '__main__':
    page.run(debug=True)
