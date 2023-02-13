import os
from deta import Deta # pip install deta
from dbsetup import getKey # pip install python-dotenv


def getDB():
    key = getKey()
    deta = Deta(key)
    db = deta.Base("monthly_reports")
    return db

def insert_user(userDetails):
    db = getDB()
    return db.put({"userDetails": userDetails})

def fetch_user():
    db = getDB()
    res = db.fetch()
    return res.items