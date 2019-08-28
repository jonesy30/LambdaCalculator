from app import app
from flask import Flask, render_template, Response, request, redirect, url_for, session
from LambdaCalculus import run_lambda_calculator

#Python file which integrates FLASK with my Lambda code

#The main screen
@app.route('/', methods=['GET','POST'])
def index():
    #If the user has posted something (a lambda expression) which needs evaluated
    if request.method == 'POST':
        #Get the incoming lambda term from the input box
        lambda_term = request.form["input-box"]
        if lambda_term != "":

            #session used for passing information between this screen and the more_information screen
            session['input'] = lambda_term
            #run the incoming lambda term through the main underlying lambda code
            returned_result,typing_context,beta_steps = run_lambda_calculator(lambda_term,request.form["evaluation-selection"])
            
            #Store the typing context and beta steps for use in the more_information page
            session['typing_context'] = typing_context
            session['beta_steps'] = beta_steps

            #Render the interface from the HMTL file
            return render_template('index.html',title='Home',result="Input = "+lambda_term+"<br>"+returned_result)
        else:
            return render_template('index.html',title='Home',result="")

    #If nothing is being evaluated just return the default screen
    return render_template('index.html',title='Home',result="")

#The more_information screen (showing type context and beta-reduction steps) accessible via a link in the main screen
@app.route('/more_information', methods=['GET','POST'])
def more_information():

    #Get the information about the last run evaluation from the session object (so it knows what it's printing)
    input_lambda = session['input']
    typing_context = session['typing_context']
    beta_details = session['beta_steps']

    #Render the information gained from the session object through the HTML file
    return render_template('more_information.html',title='More Information',input_lambda=input_lambda,typing_context=typing_context,beta_reduction=beta_details)
    