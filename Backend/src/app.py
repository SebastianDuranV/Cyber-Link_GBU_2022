from flask import Flask, json, redirect, render_template, url_for, request, flash, make_response, session, jsonify
from sql import Event, Presentation, User, Role, Nationality, LocalGroup, app, db
from flask_cors import CORS

from marchmallow import user_schema, user_schemas, ma

# Generar el requirements => pip freeze > requirements.txt

app.secret_key = 'This_is_GBU'
db.create_all()


# USER :::::::::::::::::::::::::::::::::::::::::
@app.route('/users', methods = ['POST'])
def createUser():
    id = request.json['id'] # Number of document
    names = request.json['names']
    lastName = request.json['lastName']
    dateOfBirth = request.json['dateOfBirth']
    email = request.json['email']
    vegetarian = request.json['vegetarian']
    phone = request.json['phone']
    emergencyNumber = request.json['emergencyNumber']
    user = User(id=id, names=names , email=email, lastname = lastName,
        vegetarian=vegetarian, # dateOfBirth=dateOfBirth, # falta saber como ingresar una fecha
         phone=phone, emergencyNumber=emergencyNumber)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user)

@app.route('/users', methods = ['GET'])
def getUsers():
    all_users = User.query.all()
    return user_schemas.jsonify(all_users)

@app.route('/users/<id>', methods = ['GET'])
def getUser(id):
    user = User.query.filter_by(id=id).first_or_404()
    return user_schema.jsonify(user)

@app.route('/users/<id>', methods = ['DELETE'])
def deleteUser(id):
    user = User.query.filter_by(id=id).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)


# Role ::::::::
@app.route('/role', methods = ['POST'])
def createRole():
    id = request.json['id'] # Number of document
    name = request.json['name']
    role = Role(id=id, name=name)
    db.session.add(role)
    db.session.commit()
    return user_schema.jsonify(role)

@app.route('/role', methods = ['GET'])
def getRole():
    all_role = Role.query.all()
    return user_schemas.jsonify(all_role)

@app.route('/role/<id>', methods = ['GET'])
def getRole(id):
    role = Role.query.filter_by(id=id).first_or_404()
    return user_schema.jsonify(role)

@app.route('/role/<id>', methods = ['DELETE'])
def deleteRole(id):
    role = Role.query.filter_by(id=id).first_or_404()
    db.session.delete(role)
    db.session.commit()
    return user_schema.jsonify(role)



# Nationality ::::::::::::
@app.route('/nationality', methods = ['POST'])
def createNationality():
    id = request.json['id'] # Number of document
    name = request.json['name']
    nationality = Nationality(id=id, name=name)
    db.session.add(nationality)
    db.session.commit()
    return user_schema.jsonify(nationality)

@app.route('/nationality', methods = ['GET'])
def getNationality():
    all_nationality = Nationality.query.all()
    return user_schemas.jsonify(all_nationality)

@app.route('/nationality/<id>', methods = ['GET'])
def getNationality(id):
    nationality = Nationality.query.filter_by(id=id).first_or_404()
    return user_schema.jsonify(nationality)

@app.route('/nationality/<id>', methods = ['DELETE'])
def deleteNationality(id):
    nationality = Nationality.query.filter_by(id=id).first_or_404()
    db.session.delete(nationality)
    db.session.commit()
    return user_schema.jsonify(nationality)



# LocalGroup :::::::::::
@app.route('/localGroup', methods = ['POST'])
def createLocalGroup():
    id = request.json['id'] # Number of document
    name = request.json['name']
    localGroup = LocalGroup(id=id, name=name)
    db.session.add(localGroup)
    db.session.commit()
    return user_schema.jsonify(localGroup)

@app.route('/localGroup', methods = ['GET'])
def getLocalGroup():
    all_localGroup = LocalGroup.query.all()
    return user_schemas.jsonify(all_localGroup)

@app.route('/localGroup/<id>', methods = ['GET'])
def getLocalGroup(id):
    localGroup = LocalGroup.query.filter_by(id=id).first_or_404()
    return user_schema.jsonify(localGroup)

@app.route('/localGroup/<id>', methods = ['DELETE'])
def deleteLocalGroup(id):
    localGroup = LocalGroup.query.filter_by(id=id).first_or_404()
    db.session.delete(localGroup)
    db.session.commit()
    return user_schema.jsonify(localGroup)


# Event :::::::::::
@app.route('/event', methods = ['POST'])
def createEvent():
    id = request.json['id'] # Number of document
    name = request.json['name']
    details = request.json['details']
    dateStart = request.json['dateStart']
    dateFinish = request.json['dateFinish']
    capacity = request.json['capacity']
    event = Event(id=id, name=name, details=details,dateStart=dateStart,
                dateFinish=dateFinish,capacity=capacity)
    db.session.add(event)
    db.session.commit()
    return user_schema.jsonify(event)

@app.route('/event', methods = ['GET'])
def getEvent():
    all = Event.query.all()
    return user_schemas.jsonify(all)

@app.route('/event/<id>', methods = ['GET'])
def getEvent(id):
    event = Event.query.filter_by(id=id).first_or_404()
    return user_schema.jsonify(event)

@app.route('/event/<id>', methods = ['DELETE'])
def deleteEvent(id):
    event = Event.query.filter_by(id=id).first_or_404()
    db.session.delete(event)
    db.session.commit()
    return user_schema.jsonify(event)


# Presentation ::::::::::::
@app.route('/presentation', methods = ['POST'])
def createPresentation():
    id = request.json['id'] # Number of document
    name = request.json['name']
    details = request.json['details']
    date = request.json['date']
    approved = request.json['approved']
    presentation = Presentation(id=id, name=name, details=details,date=date,
                approved=approved)
    db.session.add(presentation)
    db.session.commit()
    return user_schema.jsonify(presentation)

@app.route('/presentation', methods = ['GET'])
def getPresentation():
    all = Presentation.query.all()
    return user_schemas.jsonify(all)

@app.route('/presentation/<id>', methods = ['GET'])
def getPresentation(id):
    presentation = Presentation.query.filter_by(id=id).first_or_404()
    return user_schema.jsonify(presentation)

@app.route('/presentation/<id>', methods = ['DELETE'])
def deletePresentation(id):
    presentation = Presentation.query.filter_by(id=id).first_or_404()
    db.session.delete(presentation)
    db.session.commit()
    return user_schema.jsonify(presentation)


if __name__=='__main__':
    app.run(host= '0.0.0.0',debug=True)