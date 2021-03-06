from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:GTG24DDa@localhost/taskmanagement'
db = SQLAlchemy(app)


import flasktasks.views
import flasktasks.filters
import flasktasks.plugin_filters
import flasktasks.models
import flasktasks.logger


from flasktasks.plugins import load_plugins

load_plugins()
