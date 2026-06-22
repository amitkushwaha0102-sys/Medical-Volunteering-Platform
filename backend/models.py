from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    disease = db.Column(db.String(200), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)

class Volunteer(db.Model):
    __tablename__ = 'volunteers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    specialization = db.Column(db.String(200), nullable=False)# Rating feature placeholder
