from flask import Flask

app = Flask(__name__)
app.debug = True

from app.model.user import home as home_blueprint

app.register_blueprint(home_blueprint)