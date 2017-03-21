import os
from flask import Flask, render_template, url_for, request, redirect, flash, send_from_directory
from datetime import datetime
from flaskext.mysql import MySQL
#from flask_mysqldb import MySQL
#from application import db
#from application.models import Data
#from application.forms import EnterDBInfo, RetrieveDBInfo

app= Flask(__name__)
app.config['SECRET_KEY']= '\xce\xd0=g\x8c\xb0U\xf9\xe6V\x044\xb1aR\xb7&Z^\xa55\xeb\x02\x02'
app.config['MYSQL_HOST']='flasktest.camls7tgalgc.us-west-2.rds.amazonaws.com:3306'
app.config['MYSQL_USER']='flask'
app.config['MYSQL_PASSWORD']='flasktest'
app.config['MYSQL_DB']='flaskdb'
#mysql=MySQL(app)
mysql = MySQL()
mysql.init_app(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
	
@app.route('/')
@app.route('/index')
def index():
	cursor = mysql.get_db().cursor()
	return  render_template('index.html')
	
	  
@app.route('/add', methods=['GET','POST'])
def add():
	return render_template('add.html')
	
@app.route('/upload',methods=['POST'])
def upload():
	
		
		
# @app.route('/upload/<filename>')
# def send_image(filename):
	# return send_from_directory("images",filename)

	   # form1 = EnterDBInfo(request.form) 

       # #form2 = RetrieveDBInfo(request.form) 

    

    # if request.method == 'POST' and form1.validate():

        # data_entered = Data(notes=form1.dbNotes.data)

        # try:     

            # db.session.add(data_entered)

            # db.session.commit()        

            # db.session.close()

        # except:

            # db.session.rollback()

        # return render_template('complete.html', notes=form1.dbNotes.data)

        

    # if request.method == 'POST' and form2.validate():

        # try:   

            # num_return = int(form2.numRetrieve.data)

            # query_db = Data.query.order_by(Data.id.desc()).limit(num_return)

            # for q in query_db:

                # print(q.notes)

            # db.session.close()

        # except:

            # db.session.rollback()

        return render_template('complete.html', results=query_db, num_return=num_return)                

    

   # return render_template('index.html', form1=form1, form2=form2)
@app.errorhandler(404)
def page_not_found(e):
      return  render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
      return  render_template('500.html'), 500
	  
	  
if __name__== "__main__":
   app.run(debug=True)