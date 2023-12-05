from flask import Flask
from flask import render_template
from flask import request
import mysql.connector
from flask_cors import CORS
import json

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


@app.route("/login", methods=['GET', 'POST']) #Add User
def login():
  if request.method == 'POST':
    email = request.form['email']
    password=request.form['password']
    #print(email,studentId)
    #cur = mysql.cursor() #create a connection to the SQL instance
    
    #cur.execute('''SELECT * FROM user WHERE email=%s AND password=%s,(email,password))''')
    #user=cur.fetchone()

    #if user:
     # return "Logged In"
    #else:
     # return "Login Failed"
  else:
    return render_template('login.html')

  return '{"Result":"Success"}'




@app.route("/") #Default - Show Data
def hello(): # Name of the method
  cur = mysql.cursor() #create a connection to the SQL instance
  cur.execute('''SELECT * FROM user''') # execute an SQL statment
  rv = cur.fetchall() #Retreive all rows returend by the SQL statment
  Results=[]
  for row in rv: #Format the Output Results and add to return string
    Result={}
    Result['Username']=row[0].replace('\n',' ')
    Result['Email']=row[1]
    Result['Password']=row[2]
    Result['ID']=row[3]
    Results.append(Result)
  response={'Results':Results, 'count':len(Results)}
  ret=app.response_class(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )
  return ret #Return the data in a string format
if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080
