from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskblog'
db = SQLAlchemy(app)

# srno name email phone_num mes date
class Contacts(db.Model):

    srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    mes = db.Column(db.String(80), nullable=False)
    # date = db.Column(db.String(12), nullable=True)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=="POST"):
       
        # "ADD ENTRY TO THE DATABASE"
         name = request.form.get('name')
         email = request.form.get('email')   
         phone = request.form.get('phone')
         message = request.form.get('message')  
        #  here we fetch the data from the database now lets add the data in the database 
         entry = Contacts(name=name, phone_num=phone, mes=message, email=email)
         db.session.add(entry)
         db.session.commit()

    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/post")
def post():
    return render_template('post.html')


app.run(debug=True,port=3000)