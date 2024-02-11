from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Landlord, Tenant, Apartment, Booking

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rental_app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        # Validate required fields
        if not username or not email or not password:
            return jsonify({"error": "Missing required fields"}), 400
        
        # Check if username already exists
        if User.query.filter_by(username=username).first():
            return jsonify({"error": "Username already exists"}), 400
        
        # Check if email already exists
        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already exists"}), 400
        
        # Create new user   
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        # Return response
        response_data = {
            "message": "User created successfully",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }   
        return jsonify(response_data), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
@app.route("/login" , methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Validate required fields
    if not username or not password:
        return jsonify({"error": "Missing required fields"}), 400

    user = User.query.filter_by(username=username, password=password).first()
    if not user:
        return jsonify({"error": "Invalid username or password"}), 401

    # Return response
    response_data = {
        "message": "Login successful",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }
    return jsonify(response_data), 200


@app.route("/counties/<string:county>/apartments", methods=["GET"])
def get_counties_apartments(county):
    apartments = Apartment.query.filter_by(county=county).all()

    if not apartments:
        return jsonify({"error": "No apartments found for the specified county"}), 404
    else:
        apartments_data = [
            {
                "id": apartment.id,
                "landlord_id": apartment.landlord_id,
                "images": apartment.images,
                "address": apartment.address,
                "county": apartment.county,
                "price": apartment.price,
                "bedrooms": apartment.bedrooms,
                "description": apartment.description,
                "is_available": apartment.is_available
            }
            for apartment in apartments
        ]
        return jsonify(apartments_data), 200
    
@app.route("/add-apartment", methods=["POST"])
def add_apartment():
    data = request.get_json()
    images = data.get("images")
    county = data.get("county")
    price = data.get("price")
    bedrooms = data.get("bedrooms")
    description = data.get("description")
    is_available = data.get("is_available")

    if not images or not county or not price or not bedrooms or not description or not is_available:
        return jsonify({"error": "Missing required fields"}), 400

    apartment = Apartment(
        images=images,
        county=county,
        price=price,
        bedrooms=bedrooms,
        description=description,
        is_available=is_available
    )
    db.session.add(apartment)
    db.session.commit()

    return jsonify({"message": "Apartment added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)