import subprocess
from urllib import response
from flask import Blueprint, render_template,request,jsonify,redirect,url_for,json
import requests

views  = Blueprint(__name__,"views")

@views.route("/")    
def home():
    return render_template("index.html", name= 'Shekhar',age='35')

@views.route("/profiles/<username>")
def profiles(username):
    return render_template( "index.html", name=username)


@views.route("/profile")
def profile():
    args = request.args
    name =args.get('name')
    return render_template("index.html", name= name)

@views.route("/json")
def get_json():
    return jsonify({'name':'tim', 'coolness':10})

@views.route("/data")
def get_data():
    data= request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET",url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@views.route("/memepage")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)