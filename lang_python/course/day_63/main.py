from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase ):
  pass

db = SQLAlchemy(model_class=Base)

page = Flask(__name__)
page.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db.init_app(page)

# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# Create table schema in the database. Requires application context.
with page.app_context():
    db.create_all()



# page = Flask( __name__ )
# 
# class Base( DeclarativeBase ):
  # pass__tablename__ = 'UserRemap'
# 
# page.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# db = SQLAlchemy( model_class= Base )
# db.init_app( page )
# 
# class Book( db.Model ):
# 
  # id: Mapped[int] = mapped_column( Integer , primary_key=True )
  # name: Mapped[str] = mapped_column( String , nullable=False , unique=False )
  # author: Mapped[str] = mapped_column( String , unique=False , nullable=False )
  # rating: Mapped[float] = mapped_column( Float , nullable=False )
  # year : Mapped[str] = mapped_column( String , nullable=True )
# 
# with page.app_context():
  # db.create_all()
# 
@page.route('/' , methods=[ 'POST' , 'GET' ] )
def home():
  """
  We can even get a specific query to the datbase by inputting in a format like this.
    : data = db.session.execute( db.select( #table_name ).order_by( #condition ) ).scalar()
  We can also update the rows in the database using a specific query
  """
  # Reading the database
  result = db.session.execute( db.select( Book ).order_by( Book.rating ) )  # Obtaining result to a query in a database
  books = result.scalars()  # Getting the individual elements from the result data
  
  return render_template( 'index.html' , books = books )

@page.route("/Edit_Rating" , methods=['POST','GET'])
def Erate():
  
  if request.method=='POST':
    
    # 
    id = request.form["id"]
    
    # 
    book_upt = db.session.execute( db.select(Book).where( Book.id == id ) ).scalar()
    
    # 
    book_upt.rating = request.form["rating"]
    db.session.commit()
    
    return  redirect( url_for( 'home' ) )
  
  book_id = request.args.get( 'id' )
  book_sel = db.get_or_404( Book , book_id )
  
  return render_template( 'edit.html' , book = book_sel )

@page.route("/Delete")
def delete():
  
  id = request.args.get( key = 'id' )
  book_del = db.session.execute( db.select(Book).where( Book.id == id ) ).scalar()
  
  # Deleting the entry for the book whose id we have been given
  db.session.delete( book_del )
  db.session.commit()
  
  return redirect( url_for( 'home' ) )

  
  
@page.route("/Add" , methods=[ 'POST' , 'GET' ] )
def add():
  
  # Creating a new row in the Book table in database
  if( request.method == 'POST' ):
    book = Book(
      name = request.form.get( key = 'bookname' ),
      author = request.form.get( key = 'author' ),
      rating = request.form.get( key = 'rating' ),
      year = request.form.get( key = 'year' )
    )
    db.session.add( book )
    db.session.commit()
    return redirect( url_for( 'success' ) )

  return render_template( 'add.html' )

@page.route("/Success")
def success():
  return render_template( 'success.html' )

if __name__ == "__main__":
    page.run(debug=True)
