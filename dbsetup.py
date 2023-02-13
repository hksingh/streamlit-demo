import os
from deta import Deta # pip install deta
from dotenv import load_dotenv # pip install python-dotenv

def getKey():
    # load the environment variables
    load_dotenv()
    value = os.environ.get('ENV_PRODUCTION')
    if value == 'True':
        key = os.environ.get("DETA_KEY")
    else:
        key = os.getenv("DETA_KEY")   
    return key

