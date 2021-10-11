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
def test_disconnect():
    print('Client disconnected')

@socketio.on('yes')
def addYes():
    vota.addYes()
    emit('statusVote', vota.getStatus(), broadcast=True)

@socketio.on('no')
def addNo():
    vota.addNo()
    emit('statusVote', vota.getStatus(), broadcast=True)

@socketio.on('white')
def addWhite():
    vota.addWhite()
    emit('statusVote', vota.getStatus(), broadcast=True)