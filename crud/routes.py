from flask import  jsonify, request
import random
from crud.models import User
from crud import app,db
import os

    # {
    # "f_name":"spec",
    # "l_name":"fop",
    # "email":"sa@fok.com",
    # "pwd" : "applepie"
    # }



@app.route('/')
def home():
    return jsonify("Welcome to  USER CRUD API")

@app.route('/add', methods = ["POST"])
def add():
    try:
        no = random.randint(1,100000)
        data= request.get_json()
        if not db.retrieve(query="email",value=data["email"]):

            user = User(f_name=data["f_name"],l_name=data["l_name"],
                    email=data["email"],pwd=data["pwd"], id=no)
        
            print("user:", user)
            db.add(user.dict())

            return jsonify({
            "status":"success",
            "response": "new user added"
            })
        else:
            return jsonify({
            "status":"failed",
            "response": "Email already used"
            })
    except :
        return jsonify({
            "status":"error",
            "response": "Check your data"
            })

#not able to display list
@app.route('/search', methods = ["POST"])
def search():
    try:
        data= request.get_json()
        user = db.retrieve(query=data["query"], value=data["value"])
        if user:
            return jsonify({ "status":"success",
            "result":user})
        
        else:
            return jsonify({
            "status":"failed",
            "response": "User now found"
            })
    except :
        return jsonify({
            "status":"error",
            "response": "Check your data"
            })

@app.route('/update', methods = ["POST"])
def update():
    try:
        data= request.get_json()
        user = db.retrieve(query=data["query"], value=data["old_value"])
        print(user)
        if user:
            new_query = data["changethis"] if "changethis" in data else ""
            db.update(query=data["query"], old_value=data["old_value"],
            new_value=data["new_value"], new_query= new_query)
            return jsonify({
                "status":"success",
                "response": "data updated"})
        else:
            return jsonify({"response": "user doesn't exist"})
    except :
        return jsonify({
            "status":"error",
            "response": "Check your data"
            })

@app.route('/delete', methods = ["POST"])
def delete():
    try:
        data= request.get_json()
        user = db.retrieve(query=data["query"], value=data["value"])
        if user:
            db.delete(query=data["query"], value=data["value"])
            return jsonify({"status":"success",
                            "response": "user removed"})
        else:
            return jsonify({"status":"failed",
                            "response": "user does't exist"})
    
    except :
        return jsonify({
            "status":"error",
            "response": "Check your data"
            })


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return jsonify({"response":'Endpoint Does not exist',
                    "Current Endpoints": ["/add","/search","/update","/delete"]}   ), 404


