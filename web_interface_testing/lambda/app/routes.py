from app import app
from flask import Flask, render_template, Response, request, redirect, url_for
import hello_world_test

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        output = hello_world_test.hello_world(request.form["dabox"])
        return render_template('index.html',title='Home',user=output,result="Is anyone there?")
    
    return render_template('index.html',title='Home',user="Jonesy",result="")

@app.route("/lambda_output/", methods=['POST'])
def process_lambda():
    return "Cats cats cats"
    #output = hello_world_test.hello_world(request.form["dabox"])
    #return render_template('index.html',title='Home',user=output)
