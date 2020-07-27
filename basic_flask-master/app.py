import datetime
import uuid
import os

from flask import Flask, render_template, redirect, url_for, session, flash

from flask_session import Session

from pymongo import MongoClient
from redis import Redis

from forms import *

mongo = MongoClient("mongodb://bdd_mongo:27017/")
mongodb = mongo.testdb

redis = Redis(host="bdd_redis")

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis

Session(app)

@app.route("/", methods=["GET", "POST"])
def timeline():
    form = HomeForm()


    user = session.get('profile')

    if not user:
        return redirect(url_for('login'))
    

    if form.validate_on_submit():
        post = {
                'comment': form.comment.data,
                'user_id': user['_id']
        }
        mongodb.posts.insert_one(post)
        return redirect(url_for("timeline"))

    posts = list(mongodb.posts.find())

    for post in posts:
        post['user'] = mongodb.users.find_one({'_id' : post['user_id']})
        

    #search = mongodb.users.find_one({'_id' : post['user_id']})

    return render_template("home.html", user=user, form=form, posts=posts)
    
@app.route("/logout")
def logout():
    session['profile'] = None
    return redirect(url_for('timeline'))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        user = {
                'username': form.username.data,
                'fullname': form.fullname.data,
                'biography': form.biography.data,
                'email': form.email.data,  
                'phone': form.phone.data,  
                'password': form.password.data
        }
        mongodb.users.insert_one(user)
        return redirect(url_for("login"))
        
    return render_template("signup.html", form=form)

@app.route("/login",  methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = mongodb.users.find_one({
            'username' : form.username.data,
            'password' : form.password.data 
        })

        if not user:
            flash('Usuario no válido')
            return redirect(url_for('login'))
        
        session['profile'] = user
        return redirect(url_for('timeline'))

    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)
