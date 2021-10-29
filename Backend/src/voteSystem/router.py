from flask import Blueprint,render_template
from flask_socketio import emit, send
from app import vota
from app import socketio

vote = Blueprint('vote', __name__, url_prefix='/vote')

@vote.route('/resultsVote')
def resultsVote():
    status = vota.getStatus()
    return "yes: " + str(status['yes']) + " No: " + str(status['no']) + " White: " + str(status['white'])

@vote.route('/', methods=["GET"])
def votation():
    return render_template("vote.html")


@socketio.on('connect')
def test_connect():
    print("Client connect")

@socketio.on('disconnect')
def test_disconnect(idUser):
    vota.desconnect(idUser)
    print('Client disconnected: %s' % idUser)

@socketio.on('yes')
def addYes(idUser):
    vota.addYes(idUser)
    emit('statusVote', vota.getStatus(), broadcast=True)

@socketio.on('no')
def addNo(idUser):
    vota.addNo(idUser)
    emit('statusVote', vota.getStatus(), broadcast=True)

@socketio.on('white')
def addWhite(idUser):
    vota.addWhite(idUser)
    emit('statusVote', vota.getStatus(), broadcast=True)


@socketio.on('userConnect')
def test_connect(idUser):
    vota.connect(idUser)