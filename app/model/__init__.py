# coding:utf8
from flask_sqlalchemy import SQLAlchemy
from app import app
import pymysql

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:aa456123@127.0.0.1:3306/mydemo?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)



# if __name__ == "__main__":
   # db.create_all();
   #  print(__name__)