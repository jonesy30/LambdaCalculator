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
    # typing_context = ""

    # f_typing = open('app/static/typing_context.txt','r')
    # typing_context_list = f_typing.readlines()
    # for line in typing_context_list:
    #     typing_context = typing_context + "<p style=\"margin-bottom : 4px;\">" + line + "</p>"
    
    # beta_details = ""
    # f_beta = open('app/static/beta_reduction.txt','r')
    # beta_reduction_list = f_beta.readlines()
    # for line in beta_reduction_list:
    #     beta_details = beta_details + "<p style=\"margin-bottom : 4px;\">" + line + "</p>"

    input_lambda = session['input']
    typing_context = session['typing_context']
    beta_details = session['beta_steps']

    return render_template('more_information.html',title='More Information',input_lambda=input_lambda,typing_context=typing_context,beta_reduction=beta_details)
    