import json
import redis
from flask import Flask

app = Flask(__name__)
r = redis.StrictRedis()
mydict = {"msg": "Hello World"}
r.set("db", json.dumps(mydict))

@app.route("/")
def home():
   return json.loads(r.get("db"))["msg"]
