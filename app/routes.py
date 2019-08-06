from app import app
from flask import Flask, render_template, Response, request, redirect, url_for
#from hello_cat import hello_inner_cat
from LambdaCalculus import web_interface

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        #output = hello_world_test.hello_world(request.form["input-box"])
        lambda_term = request.form["input-box"]
        result,type_value,type_check = web_interface(lambda_term,"v")
        return render_template('index.html',title='Home',input=lambda_term,result="Result = "+result+"<br>"+"Valid typing = "+type_check+"<br>"+"Type returned = "+type_value+"<br>")
    
    return render_template('index.html',title='Home',input="enter_expression_here",user="Jonesy",result="")

@app.route("/lambda_output/", methods=['POST'])
def process_lambda():
    return "Cats cats cats"
    #output = hello_world_test.hello_world(request.form["dabox"])
    #return render_template('index.html',title='Home',user=output)
