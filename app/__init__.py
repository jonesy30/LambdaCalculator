from flask import Flask

app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

from app import routes