from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

import settings
from strategy.cls_raw import Raw
# from strategy.cls_chained import Chained

auth = HTTPBasicAuth()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = '{engine}://{username}@{host}/{db_name}'.format(
    **settings.DOLT)
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

strategy = Raw(db)

users = {
    'user': 'pass'
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return True
    return False

@app.route('/')
def hello():
	return {"hello": "world"}

@app.route('/dog')
@auth.login_required
def get_all():
    return strategy.all()

@app.route('/dog/<dog_id>', methods=['GET', 'DELETE'])
@auth.login_required
def crud(dog_id):
    if request.method == 'GET':
        return strategy.filter_by(dog_id)
    
    return strategy.delete_by(dog_id)

@app.route('/dog/<dog_name>/<dog_color>', methods=['PUT'])
@auth.login_required
def insert_entry(dog_name, dog_color):
    return strategy.insert_entry(dog_name, dog_color)

@app.route('/dog/<dog_id>/<dog_name>/<dog_color>', methods=['POST'])
@auth.login_required
def update_entry(dog_id, dog_name, dog_color):
    return strategy.update_entry(dog_id, dog_name, dog_color)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
