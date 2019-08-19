from app import app
from flask import Flask, render_template, Response, request, redirect, url_for
#from hello_cat import hello_inner_cat
from LambdaCalculus import web_interface

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        lambda_term = request.form["input-box"]
        if lambda_term != "":
            returned_result = web_interface(lambda_term,request.form["evaluation-selection"])
            
            return render_template('index.html',title='Home',result="Input = "+lambda_term+"<br>"+returned_result)
        else:
            return render_template('index.html',title='Home',result="")

    return render_template('index.html',title='Home',result="")

@app.route('/data/<path:filepath>')
def data(filepath):
    return send_from_directory('data', filepath)