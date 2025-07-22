class CarRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_car(self, car_record):
        return {
            "id": car_record [0],
            "make": car_record [1],
            "model": car_record [2],
            "year": car_record [3],
            "car_status": car_record [4],

    }
    
# Create a new car
    def create_car(self, make, model, year, car_status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.cars (make, model, year, car_status) VALUES (%s, %s, %s,%s) ",
                (make, model, year, car_status),
             )
            print("Car inserted successfully")
            return True
        
        except Exception as error:
            print(f"Error inserting a car into the database:: {error}")
            return False
        
 
 # Get all cars with optional filters
    def get_all_cars(self, filters=None):
        try:
            query = "SELECT * FROM lyfter_car_rental.cars"
            params = []

            if filters:
                conditions = []
                for key, value in filters.items():
                    conditions.append(f"{key} ILIKE %s")
                    params.append(f"%{value}%")
                query += " WHERE " + " AND ".join(conditions)

            results = self.db_manager.execute_query(query, tuple(params))
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        
        except Exception as error:
            print(f"Error fetching cars from the database: {error}")
            return False
        
    # Update car status    
    def update_car_status(self, id, car_status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET car_status = %s WHERE id = %s",
                (car_status, id),
            )
            print("Car status updated successfully")
            return True
        
        except Exception as error:
            print(f"Error updating car status in the database: {error}")
            return False    
   
        
