from flask import request, jsonify, Blueprint
from models import db, Patient, Volunteer
routes = Blueprint('routes', __name__)

@routes.route('/register-patient', methods=['POST'])
def register_patient():
    data = request.get_json()
    patient = Patient(
        name=data['name'],
        father_name=data['father_name'],
        city=data['city'],
        disease=data['disease'],
        contact_number=data['contact_number']
    )
    db.session.add(patient)
    db.session.commit()
    return jsonify({'message': 'Patient registered successfully'}), 201

@routes.route('/register-volunteer', methods=['POST'])
def register_volunteer():
    data = request.get_json()
    volunteer = Volunteer(
        name=data['name'],
        father_name=data['father_name'],
        city=data['city'],
        contact_number=data['contact_number'],
        specialization=data['specialization']
    )
    db.session.add(volunteer)
    db.session.commit()
    return jsonify({'message': 'Volunteer registered successfully'}), 201

@routes.route('/volunteers/<city>', methods=['GET'])
def get_volunteers(city):
    volunteers = Volunteer.query.filter_by(city=city).all()
    result = []
    for v in volunteers:
        result.append({
            'name': v.name,
            'specialization': v.specialization,
            'contact_number': v.contact_number
        })
    return jsonify(result), 200