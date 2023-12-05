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

@app.route("/yest")#URL leading to method
def yest(): # Name of the method
 return("Hello World!<BR/>THIS IS YET ANOTHER TEST!") #indent this line

@app.route("/register", methods=['GET', 'POST']) #Add Student
def register():
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    password=request.form['password']
    print(username,email)
    cur = mysql.cursor() #create a connection to the SQL instance
    s="INSERT INTO user(username, email, password) VALUES('{}','{}','{}');".format(username,email,password)
    app.logger.info(s)
    cur.execute(s)
    mysql.commit()
  else:
    return render_template('register.html')

  return '{"Result":"Success"}'


# @app.route("/login", methods=['GET', 'POST']) #Add Student
# def login():
#   if request.method == 'POST':
#     email = request.form['email']
#     password=request.form['password']
#     #print(email,studentId)
#     # cur = mysql.cursor() #create a connection to the SQL instance
#     # s='''INSERT INTO students(studentName, email, studentId, password) VALUES('{}','{}','{}','{}');'''.format(name,email,studentId,password)
#     # app.logger.info(s)
#     # cur.execute(s)
#     # mysql.commit()
#   else:
#     return render_template('login.html')
@app.route("/login", methods=['GET', 'POST']) #Add User
def login():
  if request.method == 'POST':
    email = request.form['email']
    password=request.form['password']
    #print(email,studentId)
    cur = mysql.cursor() #create a connection to the SQL instance
    
    cur.execute('''SELECT * FROM user WHERE email=%s AND password=%s,(email,password))''')
    record=cur.fetchone()

    if record:
      session['loggedin']=True
      session['username']=record[1];
      return redirect(url_for('home'))

    else:
      msg='Incorrect username//password. Try again!'
      
  else:
    return render_template('login.html',msg=msg)

#   return '{"Result":"Success"}'


@app.route("/") #Default - DefaultHome
def index():
  return render_template('index.html');


@app.route("/dashboard") #Dashboard
def dashboard():
  return render_template('dashboard.html', username=session['username']);

  return ret #Return the data in a string format
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080
