from flask import Flask

app = Flask(__name__, static_url_path='/static')
app.secret_key = "abc"  

from app import routes