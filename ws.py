#!/bin/python3
#Autor: Fabio Alberti
#Contact: fabiocax@gmail.com

from flask import Flask, render_template, request, jsonify
from os import popen 
import os,sys
sys.path.append('modules/')
from parole import Parole

app = Flask(__name__)

apikey=['432ref4824ijio4343233243243==']

@app.route("/")
def hello(name=None):
    return render_template('index.html',name=name)

@app.route("/updateaimlfile")
def run_aiml_build():  
    popen("python3 aiml_build.py")

@app.route("/ask", methods=['POST'])
def ask():
    pkid = request.form['apikey'].encode('utf-8').strip() 
    user = request.form['user'].encode('utf-8').strip() 
    message = request.form['messageText'].encode('utf-8').strip()
    if apikey.count(pkid.decode('utf-8')):        
        resposta=Parole().Response(message,user)
        return jsonify({'status':'OK','user':user.decode('utf-8'),'answer':resposta})
    else:
        return jsonify({'status':'ERR','user':user.decode('utf-8'),'answer':'Nao autorizado'}),401
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8089)
