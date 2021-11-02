from flask import Flask, Blueprint
from database.databaseSql import db
from api.apiDatabase import api
from components.votation import Votation 
from flask_socketio import SocketIO
from database.marchmallow import ma
from flask_cors import CORS, cross_origin

socketio = SocketIO()
vota = Votation()

def create_app():
    app = Flask(__name__)

    CORS(app)

    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/Cyber_Link_GBU_2022' # for windows
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Password1!@localhost/gbu' # for linux (ubuntu, kubuntu, etc)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'home/sebastian/Documentos/Cyber-Link_GBU_2022/Backend/src/gbu.db' # for linux (ubuntu, kubuntu, etc)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 30
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 40

    # initialize database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register blueprint routes.
    app.register_blueprint(api)
    from voteSystem.router import vote
    app.register_blueprint(vote)

    socketio.init_app(app)
    ma.init_app(app)

    return app  