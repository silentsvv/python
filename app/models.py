#coding:utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

#会员
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True) #编号
    name = db.Column(db.String(100), unique=True) #昵称
    pwd = db.Column(db.String(100)) #密码
    email = db.Column(db.String(100), unique=True) #邮箱
    phone = db.Column(db.String(11), unique=True) #手机号码
    info = db.Column(db.Text) #个人简介
    face = db.Column(db.String(255), unique=True) #头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    uuid = db.Column(db.String(255), unique=True)
    userlogs = db.relationship('Userlog', backref='user')

    def __repr__(self):
        return "<User %r>" % self.name

#会员登录日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True,default=datetime.utcnow)

    def __repr__(self):
        return "<Userlog %r>" % self.id


