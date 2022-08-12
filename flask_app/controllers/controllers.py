from flask import Flask, render_template, redirect, request, url_for
from flask_app import app
from flask_app.models.friendship import Friendship
from flask_app.models.user import User

@app.route('/')
def index():
    results = Friendship.get_all_names()
    return render_template("friendships.html", results=results, users=User.get_all())

@app.route('/create_user', methods=['GET','POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    User.save(data)
    return redirect('/')

@app.route('/create_friendship', methods=['GET','POST'])
def create_friendship():
    data = { 
        'user_id': request.form['user1_id'],
        'friend_id': request.form['user2_id']
        }
    if(Friendship.check_exists(data) == False):
        print("Exists!")
    else:
        print("Doesn't exist yet")
        Friendship.save(data)
    return redirect('/')