-- FLIGHT QUERIES

-- (F1) View all flights using destination city
SELECT flight_id, flight_number, Destination.country, Destination.city, Flights.schedule_date, Flights.schedule_time, Flights.status
FROM Flights
JOIN Destination ON Flights.destination_id = Destination.destination_id
ORDER BY Destination.city;

-- (F2) View flights by destination
SELECT flight_id, flight_number, Destination.country, Destination.city, Flights.schedule_date, Flights.schedule_time, Flights.status
FROM Flights
JOIN Destination ON Flights.destination_id = Destination.destination_id
WHERE Destination.country = 'United Kingdom'
ORDER BY Flights.schedule_date;

-- (F3) View flights by status
SELECT flight_id, flight_number, Destination.country, Destination.city, Flights.schedule_date, Flights.schedule_time, Flights.status
FROM Flights
JOIN Destination ON Flights.destination_id = Destination.destination_id
WHERE Flights.status = 'Delayed'
ORDER BY Flights.schedule_date;

-- (F4) View flights by departure date
SELECT flight_id, flight_number, Destination.country, Destination.city, Flights.schedule_date, Flights.schedule_time, Flights.status
FROM Flights
JOIN Destination ON Flights.destination_id = Destination.destination_id
WHERE Flights.schedule_date = '2026-10-18'
ORDER BY Destination.country;

-- (F5) View flights by destination and status
SELECT flight_id, flight_number, Destination.country, Destination.city, Flights.schedule_date, Flights.schedule_time, Flights.status
FROM Flights
JOIN Destination ON Flights.destination_id = Destination.destination_id
WHERE Destination.city = 'New York' AND Flights.status = 'Scheduled'
ORDER BY Flights.schedule_date;

-- (F6) Add a new flight
INSERT INTO Flights (schedule_date, schedule_time, departure_point, aircraft_type, flight_number, destination_id)
VALUES ('2026-10-27', '08:15', 'LHR', 'Boeing 787-9', 'AZ631', 7);

-- (F7) Change a flight’s departure date or time

-- (F8) Change a flight’s status


-- PILOTS QUERIES

-- (P1) Selecting 'Active' pilots
SELECT pilot_id, pilot_name, license_registration
FROM Pilots
WHERE employment_status = 'Active'
ORDER BY pilot_name;

-- (P2) Assign a pilot to a flight

-- (P3) View a pilot’s schedule AND assignment
SELECT Pilots.pilot_id, Pilots.pilot_name, Flight_Assignment.flight_role, Flights.flight_number, Flights.schedule_date, Flights.schedule_time, Flights.departure_point
FROM Pilots
JOIN Flight_Assignment ON Flight_Assignment.pilot_id = Pilots.pilot_id
JOIN Flights ON Flight_Assignment.flight_id = Flights.flight_id
WHERE Pilots.pilot_name = 'Olivia Clarke'
ORDER BY Flights.schedule_date;

-- (P4) View the crew of a flight
SELECT Flight_Assignment.flight_id, Flights.schedule_date, Flights.schedule_time, Pilots.pilot_name, Flight_Assignment.flight_role
FROM Flight_Assignment
JOIN Pilots ON Pilots.pilot_id = Flight_Assignment.pilot_id
JOIN Flights ON Flights.flight_id = Flight_Assignment.flight_id
WHERE Flight_Assignment.flight_id = 4
ORDER BY Flight_Assignment.flight_id;

-- (P5) Remove a pilot from a flight

-- (P6) View pilots with their employment status
SELECT pilot_id, pilot_name, license_registration, employment_status
FROM Pilots
WHERE employment_status = 'Retired'
ORDER BY pilot_name;


-- DESTINATIONS QUERIES

-- (D1) View all destinations
SELECT destination_id, country, city, airport_name, airport_code
FROM Destination
ORDER BY country;

-- (D2) Update a destination’s details

-- SUMMARY VIEW

-- (S1) Number of flights to each destination

-- (S2) Number of flights per pilot



