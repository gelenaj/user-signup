from flask import Flask, request, render_template, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG']=True

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")  

@app.route("/", methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify_password=request.form['verify_password']
    email=request.form['email']

   
    username_error= ""
    password_error= ""
    verify_error= ""
    email_error= ""

    wrong_combo=[".%","%@@@%","%...%", "@.", "%@@%", "@%"]
    
    if len(username)<3 or len(username)>20 or ' ' in username:
        username_error = "Username not valid: must be between 3 and 20 characters long without spaces"

    if len(password)<3 or len(password)>20 or ' ' in password:
        password_error= "Please enter a password between 3 and 20 characters long"

    if password != verify_password:
        verify_error="Your passwords do not match, please try again!" 
    
    if len(email) < 3 or len(email) >20 or email.count('@')>1 or email.count('.')>1:
        email_error = "Please enter a valid email"
    
    if any(email for word in wrong_combo):
        email_error = "Please enter a valid email" 
    if not username_error and not password_error and not verify_error:
        return redirect('/welcome?username={0}'.format(username))
    
    else:
        return render_template("index.html", username=username, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)
        
@app.route("/welcome")
def welcome():
    username=request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()