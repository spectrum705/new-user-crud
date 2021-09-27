import os
from flask import Flask
from crud.helper import Database


app = Flask(__name__)
cluster =  os.environ["mongoDb"]

db = Database(cluster)


from crud import routes