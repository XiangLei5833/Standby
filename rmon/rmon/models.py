""" rmon.model 该模块实现了所有 model 类以及相应的序列化类 """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


class Server(db.Model):
    """ Redis服务器模型 """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(512))
    host = db.Column(db.String(15))
    port = db.Column(db.Integer, default=6379)
    password = db.Column(db.String())
    updated_at = db.Column(db.DateTime, default=datetime.uctnow)
    created_at = db.Column(db.Datetime, default=datetime.uctnow)
