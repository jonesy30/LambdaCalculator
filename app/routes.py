from app import app
from flask import Flask, render_template, Response, request, redirect, url_for, session
from LambdaCalculus import web_interface

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        lambda_term = request.form["input-box"]
        if lambda_term != "":
            session['input'] = lambda_term
            returned_result,typing_context,beta_steps = web_interface(lambda_term,request.form["evaluation-selection"])
            
            session['typing_context'] = typing_context
            session['beta_steps'] = beta_steps
            return render_template('index.html',title='Home',result="Input = "+lambda_term+"<br>"+returned_result)
        else:
            return render_template('index.html',title='Home',result="")

    return render_template('index.html',title='Home',result="")

@app.route('/more_information', methods=['GET','POST'])
def more_information():

    input_lambda = session['input']
    typing_context = session['typing_context']
    beta_details = session['beta_steps']

    return render_template('more_information.html',title='More Information',input_lambda=input_lambda,typing_context=typing_context,beta_reduction=beta_details)
    