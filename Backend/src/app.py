from flask import Flask, Blueprint
from database.databaseSql import db
from api.apiDatabase import api
#from components.votation import Votation
from voteSystem.router import vote
from voteSystem.router import socketio  
from flask_socketio import SocketIO
from database.marchmallow import ma
from flask_cors import CORS, cross_origin

#socketio = SocketIO(cors_allowed_origins='*')
#vota = Votation()


#def create_app():
app = Flask(__name__)

CORS(app)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/gbu.db' # for linux (ubuntu, kubuntu, etc)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_POOL_RECYCLE'] = 30
app.config['SQLALCHEMY_POOL_TIMEOUT'] = None
app.config['SQLALCHEMY_POOL_SIZE'] = None

    # initialize database
db.init_app(app)
with app.app_context():
    db.create_all()

# Register blueprint routes.
app.register_blueprint(api)
#from voteSystem.router import vote
app.register_blueprint(vote)

socketio.init_app(app)
ma.init_app(app)

if __name__ == '__main__':
    #app.run()
    app.run(host="0.0.0.0",port=5000)
