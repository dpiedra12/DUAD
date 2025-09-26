SET search_path TO lyfter_car_rental;

--Create table Cars
--car_status: available, unavailable
CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50)  NOT NULL,
    year INT  NOT NULL,
    car_status VARCHAR(20) NOT NULL,
);

-- Popular table Cars
insert into cars (make, model, year, car_status) values ('Chevrolet', 'Blazer', 1999, 'unavailable');
insert into cars (make, model, year, car_status) values ('Chevrolet', 'SSR', 2006, 'available');
insert into cars (make, model, year, car_status) values ('Cadillac', 'Eldorado', 1997, 'unavailable');
insert into cars (make, model, year, car_status) values ('Volkswagen', 'Golf', 1996, 'available');
insert into cars (make, model, year, car_status) values ('Land Rover', 'LR3', 2009, 'unavailable');
insert into cars (make, model, year, car_status) values ('BMW', '760', 2004, 'available');
insert into cars (make, model, year, car_status) values ('Toyota', 'RAV4', 2001, 'unavailable');
insert into cars (make, model, year, car_status) values ('GMC', 'Jimmy', 1996, 'unavailable');
insert into cars (make, model, year, car_status) values ('Lexus', 'GX', 2009, 'unavailable');
insert into cars (make, model, year, car_status) values ('Aston Martin', 'Rapide', 2010, 'available');
insert into cars (make, model, year, car_status) values ('GMC', 'Yukon XL 2500', 2013, 'unavailable');
insert into cars (make, model, year, car_status) values ('Hyundai', 'Veracruz', 2009, 'unavailable');
insert into cars (make, model, year, car_status) values ('Hyundai', 'Elantra', 2011, 'unavailable');
insert into cars (make, model, year, car_status) values ('Mazda', 'B-Series', 1991, 'available');
insert into cars (make, model, year, car_status) values ('Plymouth', 'Grand Voyager', 1992, 'available');
insert into cars (make, model, year, car_status) values ('Pontiac', 'Grand Prix', 1986, 'available');
insert into cars (make, model, year, car_status) values ('Ford', 'F250', 2007, 'available');
insert into cars (make, model, year, car_status) values ('Cadillac', 'Escalade EXT', 2002, 'available');
insert into cars (make, model, year, car_status) values ('Ferrari', 'F430 Spider', 2006, 'unavailable');
insert into cars (make, model, year, car_status) values ('Chevrolet', 'Avalanche 2500', 2006, 'available');
insert into cars (make, model, year, car_status) values ('Volvo', 'C70', 1998, 'available');
insert into cars (make, model, year, car_status) values ('Dodge', 'Dakota Club', 1995, 'available');
insert into cars (make, model, year, car_status) values ('Land Rover', 'Range Rover', 2005, 'available');
insert into cars (make, model, year, car_status) values ('Hyundai', 'Excel', 1993, 'unavailable');
insert into cars (make, model, year, car_status) values ('Audi', 'A4', 2002, 'available');
insert into cars (make, model, year, car_status) values ('Mercury', 'Capri', 1991, 'unavailable');
insert into cars (make, model, year, car_status) values ('Ford', 'Mustang', 2012, 'unavailable');
insert into cars (make, model, year, car_status) values ('Pontiac', 'Grand Prix', 1992, 'unavailable');
insert into cars (make, model, year, car_status) values ('Suzuki', 'Swift', 2001, 'available');
insert into cars (make, model, year, car_status) values ('Subaru', 'Legacy', 2010, 'available');
insert into cars (make, model, year, car_status) values ('Ford', 'E-Series', 1989, 'available');
insert into cars (make, model, year, car_status) values ('Land Rover', 'Discovery', 1997, 'unavailable');
insert into cars (make, model, year, car_status) values ('Acura', 'Legend', 1993, 'available');
insert into cars (make, model, year, car_status) values ('Dodge', 'Ram 3500', 2000, 'available');
insert into cars (make, model, year, car_status) values ('Land Rover', 'Discovery', 2000, 'unavailable');
insert into cars (make, model, year, car_status) values ('Infiniti', 'QX', 2008, 'unavailable');
insert into cars (make, model, year, car_status) values ('Dodge', 'Caravan', 1997, 'unavailable');
insert into cars (make, model, year, car_status) values ('Dodge', 'D350 Club', 1992, 'unavailable');
insert into cars (make, model, year, car_status) values ('Chevrolet', 'Tahoe', 2006, 'unavailable');
insert into cars (make, model, year, car_status) values ('Chevrolet', 'Impala', 2002, 'available');
insert into cars (make, model, year, car_status) values ('Chevrolet', 'Corsica', 1995, 'available');
insert into cars (make, model, year, car_status) values ('Ford', 'F250', 1984, 'unavailable');
insert into cars (make, model, year, car_status) values ('Ford', 'Probe', 1991, 'unavailable');
insert into cars (make, model, year, car_status) values ('Mercedes-Benz', 'S-Class', 1987, 'available');
insert into cars (make, model, year, car_status) values ('Dodge', 'Ram 3500', 2008, 'available');
insert into cars (make, model, year, car_status) values ('Mercedes-Benz', 'SL-Class', 1996, 'available');
insert into cars (make, model, year, car_status) values ('Lexus', 'IS-F', 2010, 'available');
insert into cars (make, model, year, car_status) values ('Mitsubishi', 'Lancer Evolution', 2008, 'available');
insert into cars (make, model, year, car_status) values ('Pontiac', 'Grand Am', 1990, 'available');
insert into cars (make, model, year, car_status) values ('Jeep', 'Wrangler', 2000, 'unavailable');
