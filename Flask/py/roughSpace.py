
from flask import Flask, render_template 
import os
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

myDir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(myDir, 'mydb.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# print(myDir)

class Discord(db.Model):
    __tablename__ = 'DiscordInfo'
    realName = db.Column(db.Text, primary_key = True)
    name1 = db.Column(db.Text)
    name2 = db.Column(db.Text)
    
    def __init__ (self, realName, name1, name2):
        self.realName = realName
        self.name1 = name1
        self.name2 = name2

    def __repr__(self):
        return f"{self.realName} aka {self.name1} & {self.name2}"
 


