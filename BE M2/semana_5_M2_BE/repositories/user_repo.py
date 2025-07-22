

class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "name": user_record[1],
            "username": user_record[2],
            "email": user_record[3],
            "birth_date": user_record[4],
            "account_status": user_record[5],

    }

    # Get all users with optional filters
    def get_all_users(self, filters=None):
        try:
            query = "SELECT * FROM lyfter_car_rental.users"
            params = []

            if filters:
                conditions = []
                for key, value in filters.items():
                    conditions.append(f"{key} ILIKE %s")  
                    params.append(f"%{value}%")
                query += " WHERE " + " AND ".join(conditions)

            results = self.db_manager.execute_query(query, tuple(params))
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        
        except Exception as error:
            print(f"Error fetching users from the database: {error}")
            return False

    # Create a new user
    def create_user(self, name, email, username, password, birth_date, account_status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users (name, email, username, password, birth_date, account_status) VALUES (%s, %s, %s,%s, %s, %s) ",
                (name, email, username, password, birth_date, account_status),
            
            )
            print("User inserted successfully")
            return True
        
        except Exception as error:
            print(f"Error inserting a user into the database:: {error}")
            return False
        
    # Update user state    
    def update_user_state(self, id, account_status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status = %s WHERE id = %s",
                (account_status, id),
            )
            print("User state updated successfully")
            return True
        
        except Exception as error:
            print(f"Error updating user state in the database: {error}")
            return False    

    # Flag user as delinquent    
    def flag_user_as_delinquent(self, id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status = 'delinquent' WHERE id = %s",
                (id,),
            )
            print("User flagged as delinquent successfully")
            return True
        
        except Exception as error:
            print(f"Error flagging user as delinquent in the database: {error}")
            return False    
