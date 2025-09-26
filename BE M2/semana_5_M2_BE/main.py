from flask import Flask, request, jsonify
from db import PgManager
from repositories.user_repo import UserRepository
from repositories.car_repo import CarRepository
from repositories.rental_repo import RentalRepository

app = Flask(__name__)
# Initialize the database manager with connection parameters
db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="1234",
    host="localhost"
)

# Create an instance of UserRepository with the database manager
user_repo = UserRepository(db_manager)
car_repo = CarRepository(db_manager)
rental_repo = RentalRepository(db_manager)

# Insert a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    success = user_repo.create_user(
        data["name"],
        data["email"],
        data["username"],
        data["password"],
        data["birth_date"],
        data["account_status"],
    )

    if success:
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"error": "Error creating user"}), 500

# Insert a new car
@app.route("/cars", methods=["POST"])
def create_car():
    data = request.get_json()

    success = car_repo.create_car(
        data["make"],
        data["model"],
        data["year"],
        data["car_status"],
    )
    if success:
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"error": "Error creating user"}), 500
    
# Insert a new rental
@app.route("/rentals", methods=["POST"])
def create_rental():
    data = request.get_json()
    success = rental_repo.create_rental(
        data["user_id"],
        data["car_id"],
        data["rental_status"],
    )

    if success:
        return jsonify({"message": "Rental created successfully"}), 201
    else:
        return jsonify({"error": "Error creating rental"}), 500      

# Update car status
@app.route("/cars/<int:id>", methods=["PATCH"])
def update_car_status(id):
   
    data = request.get_json()
    
    success = car_repo.update_car_status(id, data["car_status"])

    if success:
        return jsonify({"message": "Car status updated successfully"}), 200
    else:
        return jsonify({"error": "Error updating car  status"}), 500
    
# Update user status
@app.route("/users/<int:id>", methods=["PATCH"])
def update_user_status(id):
   
    data = request.get_json()
    
    success = user_repo.update_user_state(id, data["account_status"])

    if success:
        return jsonify({"message": "User status updated successfully"}), 200
    else:
        return jsonify({"error": "Error updating user status"}), 500
    
# Complete rental and update car status to available
@app.route("/rentals/<int:id>/complete", methods=["PATCH"])
def complete_rental(id):
    
    success = rental_repo.complete_rental_and_put_car_available(id)

    if success:
        return jsonify({"message": "Rental completed successfully"}), 200
    else:
        return jsonify({"error": "Error completing rental"}), 500

    
# Update rental status
@app.route("/rentals/<int:id>", methods=["PATCH"])
def update_rental_status(id):
   
    data = request.get_json()
    
    success = rental_repo.update_rental_status(id, data["rental_status"])

    if success:
        return jsonify({"message": "Rental status updated successfully"}), 200
    else:
        return jsonify({"error": "Error updating rental  status"}), 500        

# Flag user as delinquent
@app.route("/users/<int:id>/flag", methods=["PATCH"])
def flag_user_as_delinquent(id):
    
    success = user_repo.flag_user_as_delinquent(id)

    if success:
        return jsonify({"message": "User flagged as delinquent successfully"}), 200
    else:
        return jsonify({"error": "Error flagging user as delinquent"}), 500
    
    
# Get all users with filters
@app.route("/users", methods=["GET"])
def get_users():
    filters = request.args.to_dict()  
    users = user_repo.get_all_users(filters)
    
    if users:
        return jsonify(users), 200
    else:
        return jsonify({"error": "No users found"}), 404

# Get all cars with filters
@app.route("/cars", methods=["GET"])
def get_cars():
    filters = request.args.to_dict()
    cars = car_repo.get_all_cars(filters)
    
    if cars:
        return jsonify(cars), 200
    else:
        return jsonify({"error": "No cars found"}), 404

# Get all rentals with filters
@app.route("/rentals", methods=["GET"])
def get_rentals():
    filters = request.args.to_dict()
    rentals = rental_repo.get_all_rentals(filters)
   
    if rentals:
        return jsonify(rentals), 200
    else:
        return jsonify({"error": "No rentals found"}), 404
    

if __name__ == "__main__":
    app.run(debug=True)
