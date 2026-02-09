from flask import Flask, render_template
import post
from requests import get

URL='https://api.npoint.io/c790b4d5cab58020d391'
data=get(URL).json()

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html",Dt=data)

@app.route('/post/a=<int:id>')
def blog(id):
  	return render_template('post.html',val=data[id-1])

if __name__ == "__main__":
    app.run(debug=True)
