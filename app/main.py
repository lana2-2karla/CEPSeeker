from flask import Flask
from routes import main_blueprint

app = Flask(__name__)
app.register_blueprint(main_blueprint)

app.config.from_pyfile('config.py')

app.run()
