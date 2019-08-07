from app import app
from flask import Flask, render_template, Response, request, redirect, url_for
#from hello_cat import hello_inner_cat
from LambdaCalculus import web_interface

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        lambda_term = request.form["input-box"]
        if lambda_term != "":
            #result,type_value,type_check = web_interface(lambda_term,request.form["evaluation-selection"])
            returned_result = web_interface(lambda_term,request.form["evaluation-selection"])
            
            if isinstance(returned_result,str):
                return render_template('index.html',title='Home',input=lambda_term,result=returned_result)
            else:
                result = returned_result[0]
                type_value = returned_result[1]
                type_check = returned_result[2]
                return render_template('index.html',title='Home',input=lambda_term,result="Result = "+result+"<br>"+"Valid typing = "+type_check+"<br>"+"Type returned = "+type_value+"<br>")

        else:
            return render_template('index.html',title='Home',input="enter_expression_here",result="")

    return render_template('index.html',title='Home',input="enter_expression_here",result="")
