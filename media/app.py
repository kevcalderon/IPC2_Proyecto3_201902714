from flask import Flask, render_template, request, redirect, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import json
import os
app= Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/ipc2', methods=['GET','POST'])
def main_function():
    if request.method == 'GET':
        return jsonify({"status_code": 200, "mensaje": "Conferencia Python Flask"})
    elif request.method == 'POST':
        params=json.loads(request.data)
        print(params)
        cadena="Servidor creado con "+params['tema']+" el cual utiliza el lenguaje "+params['lenguaje']
        return jsonify({"status": 200, "mensaje": cadena})


@app.route("/saludo",methods=["GET","POST"])
def saludo():
    saludo=""
    if request.method=="POST":
        saludo=request.form.get("saludo")
        return f"Hola {saludo}"
    elif request.method=="GET":
        return f"Hola {saludo}"

if __name__=="__main__":
    app.run(debug=True)