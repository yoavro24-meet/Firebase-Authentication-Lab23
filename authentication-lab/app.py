from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  'apiKey': "AIzaSyCE02MCZrTpF2pzwndf6XPqy1yZgeG-jrA",
  "authDomain": "yoyo-75359.firebaseapp.com",
  "projectId": "yoyo-75359",
  "storageBucket": "yoyo-75359.appspot.com",
  "messagingSenderId": "1020780344618",
  "appId": "1:1020780344618:web:02437bb37ac22b04689a53",
  "measurementId": "G-M96DT037N5",
  'databaseURL':'https://yoyo-75359-default-rtdb.europe-west1.firebasedatabase.app/'    
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for("add_tweet"))
        except Exception as e:
            print("ERROR IN SIGNIN", e)
            error = "sorry u didnt succeed"

    return render_template("signin.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        fullname = request.form['fullname']
        username = request.form["username"]
        bio = request.form['bio']
        
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email,password)
            UID = login_session['user']['localId']
            user = {'email':email,'fullname':fullname,'username':username,'bio':bio}
            db.child("Users").child(UID).set(user)
            return redirect(url_for("add_tweet"))
        except:
            error = "sorry u didnt succeed"
            print(error)
    return render_template("signup.html")

@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    error = 'you didnt succeed'
    if request.method == 'POST':
        Title = request.form['title']
        Text = request.form["text"]
        try:
            UID = login_session['user']['localId'] 
            tweet = {'title':Title,'text':Text,'UID':UID}
            db.child("Tweets").push(tweet)
            return  redirect(url_for('showtwt')) 
        except:
           print(error)
    return render_template("add_tweet.html")

@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))

@app.route('/all_tweets')
def showtwt():
  Tweets = db.child('Tweets').get().val()
  return render_template('tweets.html',Twt = Tweets)


if __name__ == '__main__':
    app.run(debug=True)