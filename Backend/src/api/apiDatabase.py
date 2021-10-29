from flask import Blueprint, request
from database.marchmallow import user_schema, user_schemas, ma
from database.databaseSql import db, User, Role, Event, Presentation, Nationality, LocalGroup

api = Blueprint('api',__name__,url_prefix='/api')

# USER :::::::::::::::::::::::::::::::::::::::::
@api.route('/users', methods = ['POST'])
def createUser():
    id = request.json['id'] # Number of document (rut)
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

    try:
        db.session.commit()
    except:
        return "Usuario mal enviado, o ya existe"
    
    return user_schema.jsonify(user)

@api.route('/users', methods = ['GET'])
def getUsers():
    all_users = User.query.all()
    return user_schemas.jsonify(all_users)

@api.route('/users/<id>', methods = ['GET'])
def getUser(id):
    user = User.query.filter_by(id=id).first_or_404()
    return user_schema.jsonify(user)

@api.route('/users', methods = ['DELETE'])
def deleteUser():
    id = request.json['id']
    user = User.query.filter_by(id=id).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)


# Role ::::::::
@api.route('/role', methods = ['POST'])
def createRole():
    id = request.json['id'] # Number of document
    name = request.json['name']
    role = Role(id=id, name=name)
    db.session.add(role)
    db.session.commit()
    return user_schema.jsonify(role)

@api.route('/role', methods = ['GET'])
def getRole():
    all_role = Role.query.all()
    return user_schemas.jsonify(all_role)

@api.route('/role/<id>', methods = ['GET'])
def getRoles(id):
    role = Role.query.filter_by(id=id).first_or_404()
    return user_schema.jsonify(role)

@api.route('/role/<id>', methods = ['DELETE'])
def deleteRole(id):
    role = Role.query.filter_by(id=id).first_or_404()
    db.session.delete(role)
    db.session.commit()
    return user_schema.jsonify(role)



# Nationality ::::::::::::
@api.route('/nationality', methods = ['POST'])
def createNationality():
    #id = request.json['id'] # Number of document
    name = request.json['name']
    nationality = Nationality(id=id, name=name)
    db.session.add(nationality)
    db.session.commit()
    return user_schema.jsonify(nationality)

@api.route('/nationality', methods = ['GET'])
def getNationality():
    all_nationality = Nationality.query.all()
    return user_schemas.jsonify(all_nationality)

@api.route('/nationality/<id>', methods = ['GET'])
def getNationalitys(id):
    nationality = Nationality.query.filter_by(id=id).first_or_404()
    return user_schema.jsonify(nationality)

@api.route('/nationality/<id>', methods = ['DELETE'])
def deleteNationality(id):
    nationality = Nationality.query.filter_by(id=id).first_or_404()
    db.session.delete(nationality)
    db.session.commit()
    return user_schema.jsonify(nationality)



# LocalGroup :::::::::::
@api.route('/localGroup', methods = ['POST'])
def createLocalGroup():
    #id = request.json['id'] # Number of document
    name = request.json['name']
    localGroup = LocalGroup(id=id, name=name)
    db.session.add(localGroup)
    db.session.commit()
    return user_schema.jsonify(localGroup)

@api.route('/localGroup', methods = ['GET'])
def getLocalGroup():
    all_localGroup = LocalGroup.query.all()
    return user_schemas.jsonify(all_localGroup)

@api.route('/localGroup/<id>', methods = ['GET'])
def getLocalGroups(id):
    localGroup = LocalGroup.query.filter_by(id=id).first_or_404()
    return user_schema.jsonify(localGroup)

@api.route('/localGroup/<id>', methods = ['DELETE'])
def deleteLocalGroup(id):
    localGroup = LocalGroup.query.filter_by(id=id).first_or_404()
    db.session.delete(localGroup)
    db.session.commit()
    return user_schema.jsonify(localGroup)


# Event :::::::::::
@api.route('/event', methods = ['POST'])
def createEvent():
    #id = request.json['id'] # Number of document
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

@api.route('/event', methods = ['GET'])
def getEvent():
    all = Event.query.all()
    return user_schemas.jsonify(all)

@api.route('/event/<id>', methods = ['GET'])
def getEvents(id):
    event = Event.query.filter_by(id=id).first_or_404()
    return user_schema.jsonify(event)

@api.route('/event/<id>', methods = ['DELETE'])
def deleteEvent(id):
    event = Event.query.filter_by(id=id).first_or_404()
    db.session.delete(event)
    db.session.commit()
    return user_schema.jsonify(event)


# Presentation ::::::::::::
@api.route('/presentation', methods = ['POST'])
def createPresentation():
    #id = request.json['id'] # Number of document
    name = request.json['name']
    details = request.json['details']
    date = request.json['date']
    apiroved = request.json['apiroved']
    presentation = Presentation(id=id, name=name, details=details,date=date,
                apiroved=apiroved)
    db.session.add(presentation)
    db.session.commit()
    return user_schema.jsonify(presentation)

@api.route('/presentation', methods = ['GET'])
def getPresentation():
    all = Presentation.query.all()
    return user_schemas.jsonify(all)

@api.route('/presentation/<id>', methods = ['GET'])
def getPresentations(id):
    presentation = Presentation.query.filter_by(id=id).first_or_404()
    return user_schema.jsonify(presentation)

@api.route('/presentation/<id>', methods = ['DELETE'])
def deletePresentation(id):
    presentation = Presentation.query.filter_by(id=id).first_or_404()
    db.session.delete(presentation)
    db.session.commit()
    return user_schema.jsonify(presentation)
