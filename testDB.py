from deta import Deta
import os
from dbsetup import getKey

deta = Deta(getKey())

def run():
    users = deta.Base("users")
    users.insert({
        "name": "hemant", "title": "Engineer"
    })

    fetch_res = users.fetch({"name": "hemant"})
    for item in fetch_res.items:
        print(item["key"], item)
    print('hello world')

if __name__ == '__main__':
    run()