from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == "POST"
        email = request.form['email']
        passsword = request.form['password']
        try:
            login_session['user'] = 
            auth.create_user_with_email_and_password(email,password)
            return redirect(url_for("add_tweet"))
        except:
            error = "sorry u didnt succeed"
            return render_template("signin.html")

    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == "POST"
        email = request.form['email']
        passsword = request.form['password']
        try:
            login_session['user'] = 
            auth.create_user_with_email_and_password(email,password)
            return redirect(url_for("add_tweet"))
        except:
            error = "sorry u didnt succeed"
            return render_template("signup.html")

@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)