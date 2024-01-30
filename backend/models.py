from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy instance
db = SQLAlchemy()

# User model representing a user in the system
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Landlord model representing a landlord in the system
class Landlord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Define a relationship with the User model
    user = db.relationship('User', backref=db.backref('landlord', lazy=True))

# Tenant model representing a tenant in the system
class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Define a relationship with the User model
    user = db.relationship('User', backref=db.backref('tenant', lazy=True))

# Apartment model representing a rental property
class Apartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    landlord_id = db.Column(db.Integer, db.ForeignKey('landlord.id'), nullable=False)
    images = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    county = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    is_available = db.Column(db.Boolean, default=True)

    # Define a relationship with the Landlord model
    landlord = db.relationship('Landlord', backref=db.backref('apartments', lazy=True))

# Booking model representing a booking made by a tenant for an apartment
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'), nullable=False)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)

    # Define relationships with the Tenant and Apartment models
    tenant = db.relationship('Tenant', backref=db.backref('bookings', lazy=True))
    apartment = db.relationship('Apartment', backref=db.backref('bookings', lazy=True))

