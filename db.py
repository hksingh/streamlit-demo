import os
from deta import Deta # pip install deta
from dotenv import load_dotenv # pip install python-dotenv

# load the environment variables
# load_dotenv(".env")
DETA_KEY = os.environ.get("DETA_KEY")
# DETA_KEY = "b0nqz419_JTjja4Xy6oVaUKn4yy53N76QJvAyMUGf"

def getKey():
    return os.environ.get("DETA_KEY")

def getDB():
    db = Deta.Base("monthly_reports")
    return db

def insert_user(userDetails):
    db = getDB()
    return db.put({"userDetails": userDetails})

def fetch_user():
    db = getDB()
    res = db.fetch()
    return res.items