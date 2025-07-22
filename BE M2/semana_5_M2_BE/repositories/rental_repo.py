class RentalRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_rental(self, rental_record):
        return {
            "id": rental_record [0],
            "user_id": rental_record [1],
            "car_id": rental_record [2],
            "rental_date": rental_record [3],
            "rental_status": rental_record [4],

    }
    
# Create a new rental
    def create_rental(self, user_id, car_id, rental_date, rental_status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.rentals (user_id, car_id,  rental_status) VALUES (%s, %s,%s,%s) ",
                (user_id, car_id,rental_date,  rental_status),            
            )
            print("Rental inserted successfully")
            return True
        
        except Exception as error:
            print(f"Error inserting a rental into the database:: {error}")
            return False
        
    # Get all rentals with optional filters   
    def get_all_rentals(self, filters=None):
        try:
            query = "SELECT * FROM lyfter_car_rental.rentals"
            params = []

            if filters:
                conditions = []
                for key, value in filters.items():
                    conditions.append(f"{key} ILIKE %s")
                    params.append(f"%{value}%")
                query += " WHERE " + " AND ".join(conditions)

            results = self.db_manager.execute_query(query, tuple(params))
            formatted_results = [self._format_rental(result) for result in results]
            return formatted_results
        
        except Exception as error:
            print(f"Error fetching rentals from the database: {error}")
            return False   
        
    # Update rental status    
    def update_rental_status(self, id, rental_status):
            try:
                self.db_manager.execute_query(
                    "UPDATE lyfter_car_rental.rentals SET rental_status = %s WHERE id = %s",
                    (rental_status, id),
                )
                print("Rental status updated successfully")
                return True
            
            except Exception as error:
                print(f"Error updating rental status in the database: {error}")
                return False
            
    # Complete rental and put car available        
    def complete_rental_and_put_car_available(self, id):
        try:
            # Update the rental status to 'completed'
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.rentals SET rental_status = 'completed' WHERE id = %s",
                (id,),
            )
            # Update the car status to 'available'
            
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET car_status = 'available' WHERE id = (SELECT car_id FROM lyfter_car_rental.rentals WHERE id = %s)",
                (id,),

            )

            print("Rental completed successfully")
            return True
        
        except Exception as error:
            print(f"Error completing rental in the database: {error}")
            return False