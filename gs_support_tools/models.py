from enum import unique
from . import db
from flask import session
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(50), unique=True)

    def get_id(self):
        return self.user_id


class SR_lists(db.Model):
    __tablename__ = 'sr_lists'
    sr_id = db.Column(db.Integer, autoincrement=True)
    user_id = db.Column(db.Integer)
    number = db.Column(db.Integer, unique=True, primary_key=True)
    subject = db.Column(db.String(50))
    status = db.Column(db.String(15))
    substatus = db.Column(db.String(15))
    idle = db.Column(db.Float)


db.create_all()
# Test SR_lists


def test_sr():
    for i in range(10):
        user_id = 1
        number = 11111111110 + i
        subject = "Test Subject " + str(i)
        status = "Open"
        substatus = "Working"
        idle = 0.1 + i
        sr_lists = SR_lists(user_id=user_id, number=number, subject=subject,
                            status=status, substatus=substatus, idle=idle)
        db.session.add(sr_lists)
    db.session.commit()
