from flask import Flask
from flask import render_template
from flask import request
import mysql.connector
from flask_cors import CORS
import json
from flask import session, redirect, url_for


mysql = mysql.connector.connect(user='web', password='webPass',
  host='127.0.0.1',
  database='user_register')



from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
app = Flask(__name__)
CORS(app)
# My SQL Instance configurations
# Change the HOST IP and Password to match your instance configurations

app.secret_key="secret key"

@app.route("/test")#URL leading to method
def test(): # Name of the method
 return("Hello World!<BR/>THIS IS ANOTHER TEST!") #indent this line

@app.route("/register", methods=['GET', 'POST']) #Add Student
def register():
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    phone=request.form['phone']
    password=request.form['password']
    print(username,email)
    cur = mysql.cursor() #create a connection to the SQL instance
    s="INSERT INTO user(username, email, password, phone) VALUES('{}','{}','{}','{}');".format(username,email,password,phone)
    app.logger.info(s)
    cur.execute(s)
    mysql.commit()
  else:
    return render_template('register.html')

  return '{"Result":"Success"}'


@app.route("/login", methods=['GET', 'POST'])
def login():
  msg=''
  if request.method == 'POST':
    email = request.form['email']
    password=request.form['password']
    cur = mysql.cursor() #create a connection to the SQL instance
    
    cur.execute('SELECT * FROM user WHERE email=%s AND password=%s',(email,password))
    record=cur.fetchone()

    if record:
      session['loggedin']=True
      session['username']=record[0];

      if record[1]=='firstadmin@mydbs.ie' or record[1]=='secondadmin@mydbs.ie' or record[1]=='thirdadmin@mydbs.ie' or record[1]=='forthadmin@mydbs.ie':
        #if logged n as admin, goto admin dashboard
        return redirect(url_for('dashboard'))
        
      else:
        #if logged in as user, goto user dashboard
        return redirect(url_for('dashboard'))

    else:
      msg='Incorrect username/password. Try again!'
      return render_template('login.html',msg=msg)
    
      
  return render_template('login.html',msg=msg)

@app.route("/logout")
def logout():
  session.pop('loggedin', None)
  session.pop('username', None)
  return redirect(url_for('login'))


@app.route("/") #Default - DefaultHome
def index():
  return render_template('index.html');


@app.route("/dashboard") #Dashboard
def dashboard():
  return render_template('dashboard.html', username=session['username']);

  return ret #Return the data in a string format
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080
