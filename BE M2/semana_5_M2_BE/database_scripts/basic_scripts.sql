SET search_path TO lyfter_car_rental;

--a.Un script que agregue un usuario nuevo
INSERT INTO users (name, email, username, password, birth_date, account_status) 
VALUES ('Danny', 'danny@xinhuanet.com', 'dpiedra', 'hL0%s}jT=YH_}', '04/20/1990', 'active');

--b.Un script que agregue un automovil nuevo
INSERT  INTO cars (make, model, year, car_status) 
VALUES ('Toyota', 'Corolla', 2024, 'available');

-- c.Un script que cambie el estado de un usuario
UPDATE users
SET account_status = 'inactive'
WHERE id = 51;

--d.Un script que cambie el estado de un automovil
UPDATE cars
SET car_status = 'unavailable'
WHERE id = 51;


--e.Un script que genere un alquiler nuevo con los datos de un usuario y un automovil
INSERT INTO rentals (user_id,car_id, rental_status) 
VALUES (51,51,'active');

--f.Un script que confirme la devolución del auto al completar el alquiler, 
--colocando el auto como disponible y completando el estado del alquiler

UPDATE rentals
SET rental_status = 'completed'
WHERE id = 1;

UPDATE cars
SET car_status = 'available'
WHERE id = (
    SELECT car_id FROM rentals WHERE id = 51
);

--g.Un script que deshabilite un automovil del alquiler
UPDATE cars
SET car_status = 'unavailable'
WHERE id = 51;


--h.Un script que obtenga todos los automoviles alquilados, y otro que obtenga todos los disponibles.
SELECT * FROM rentals WHERE rental_status = 'active';

SELECT * FROM cars WHERE car_status = 'available'
