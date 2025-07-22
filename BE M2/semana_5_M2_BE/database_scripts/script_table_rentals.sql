SET search_path TO lyfter_car_rental;

--Create table Rentals
--rental_status:active, completed, cancelled
CREATE TABLE rentals (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    car_id INT NOT NULL REFERENCES cars(id) ON DELETE CASCADE,
	rental_date DATE NOT NULL DEFAULT CURRENT_DATE,
	rental_status VARCHAR(20) NOT NULL

);