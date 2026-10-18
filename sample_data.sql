PRAGMA foreign_keys = ON;

-- Sample data for the Flight Management database
-- Generated with AI, as permitted by the brief (AI may be used to populate the database).
-- The system belongs to a single fictional airline, Azure Global Airways (flight code AZ),
-- so the airline is not stored as a column. Flight numbers, pilots and licences are fictional.
-- Airports, cities and airport codes are real.
-- The airline is assumed to be based at London Heathrow (LHR).
-- Insert order matters: Destination and Pilots first, then Flights, then Flight_Assignment.

-- Destinations: IDs 1 to 12, in the order listed
INSERT INTO Destination (airport_code, airport_name, city, country) VALUES
('LHR', 'Heathrow Airport', 'London', 'United Kingdom'),
('CDG', 'Paris Charles de Gaulle Airport', 'Paris', 'France'),
('AMS', 'Amsterdam Airport Schiphol', 'Amsterdam', 'Netherlands'),
('FRA', 'Frankfurt Airport', 'Frankfurt', 'Germany'),
('JFK', 'John F. Kennedy International Airport', 'New York', 'United States'),
('YYZ', 'Toronto Pearson International Airport', 'Toronto', 'Canada'),
('DXB', 'Dubai International Airport', 'Dubai', 'United Arab Emirates'),
('SIN', 'Singapore Changi Airport', 'Singapore', 'Singapore'),
('HND', 'Tokyo Haneda Airport', 'Tokyo', 'Japan'),
('SYD', 'Sydney Kingsford Smith Airport', 'Sydney', 'Australia'),
('CPT', 'Cape Town International Airport', 'Cape Town', 'South Africa'),
('MNL', 'Ninoy Aquino International Airport', 'Manila', 'Philippines');

-- Pilots: IDs 1 to 12
-- Licence format: issuing country - licence type - number
-- ATPL pilots can act as Captain; CPL pilots fly as First Officer
-- Pilot 10 is Active but has no flights (shows as Available)
-- Pilot 11 is On leave, pilot 12 is Retired
INSERT INTO Pilots (pilot_name, license_registration, employment_status) VALUES
('Olivia Clarke', 'UK-ATPL-20871', 'Active'),
('Liam O''Connor', 'IE-CPL-31452', 'Active'),
('Sofia Rossi', 'IT-ATPL-19634', 'Active'),
('Daniel Okafor', 'UK-CPL-32018', 'Active'),
('Hannah Becker', 'DE-ATPL-22590', 'Active'),
('James Whitfield', 'UK-ATPL-18277', 'Active'),
('Priya Sharma', 'UK-CPL-33741', 'Active'),
('Lucas Martin', 'FR-CPL-34106', 'Active'),
('Maria Santos', 'PH-ATPL-21359', 'Active'),
('Noah Williams', 'AU-CPL-35220', 'Active'),
('Aiko Tanaka', 'JP-ATPL-17802', 'On leave'),
('Robert Hughes', 'UK-ATPL-15467', 'Retired');

-- Flights: IDs 1 to 15, from 16 to 25 October 2026
-- Status is left out, so these start as 'Scheduled'
INSERT INTO Flights (schedule_date, schedule_time, departure_point, aircraft_type, flight_number, destination_id) VALUES
('2026-10-16', '07:10', 'LHR', 'Airbus A320neo', 'AZ201', 2),
('2026-10-16', '21:30', 'LHR', 'Boeing 787-9', 'AZ801', 8),
('2026-10-17', '08:05', 'LHR', 'Airbus A320neo', 'AZ221', 3),
('2026-10-17', '11:20', 'AMS', 'Airbus A320neo', 'AZ222', 1),
('2026-10-18', '09:45', 'LHR', 'Airbus A350-1000', 'AZ101', 5),
('2026-10-18', '12:15', 'LHR', 'Airbus A321neo', 'AZ241', 4),
('2026-10-18', '21:55', 'LHR', 'Boeing 777-300ER', 'AZ901', 10),
('2026-10-19', '10:30', 'LHR', 'Boeing 787-9', 'AZ601', 7),
('2026-10-19', '13:40', 'CDG', 'Airbus A320neo', 'AZ202', 1),
('2026-10-20', '11:00', 'LHR', 'Boeing 787-9', 'AZ121', 6),
('2026-10-20', '20:15', 'LHR', 'Airbus A350-1000', 'AZ701', 9),
('2026-10-21', '19:40', 'LHR', 'Boeing 787-9', 'AZ851', 12),
('2026-10-21', '18:25', 'LHR', 'Boeing 777-300ER', 'AZ501', 11),
('2026-10-23', '07:40', 'LHR', 'Airbus A320neo', 'AZ243', 4),
('2026-10-25', '22:00', 'SIN', 'Boeing 787-9', 'AZ802', 1);

-- Flights 16 to 18: a status other than 'Scheduled'
INSERT INTO Flights (schedule_date, schedule_time, departure_point, aircraft_type, flight_number, destination_id, status) VALUES
('2026-10-22', '08:20', 'LHR', 'Airbus A321neo', 'AZ223', 3, 'Delayed'),
('2026-10-24', '07:10', 'LHR', 'Airbus A320neo', 'AZ203', 2, 'Cancelled'),
('2026-10-24', '10:30', 'LHR', 'Airbus A350-1000', 'AZ103', 5, 'Rescheduled');

-- Flight assignments: each flight has a Captain and a First Officer
-- Long-haul flights (Singapore, Sydney, Tokyo, Manila, Cape Town) also carry a Reserve pilot
INSERT INTO Flight_Assignment (flight_id, pilot_id, flight_role) VALUES
(1, 1, 'Captain'), (1, 2, 'First Officer'),
(2, 3, 'Captain'), (2, 4, 'First Officer'), (2, 5, 'Reserve'),
(3, 6, 'Captain'), (3, 7, 'First Officer'),
(4, 6, 'Captain'), (4, 7, 'First Officer'),
(5, 1, 'Captain'), (5, 8, 'First Officer'),
(6, 9, 'Captain'), (6, 2, 'First Officer'),
(7, 6, 'Captain'), (7, 7, 'First Officer'), (7, 5, 'Reserve'),
(8, 1, 'Captain'), (8, 8, 'First Officer'),
(9, 9, 'Captain'), (9, 2, 'First Officer'),
(10, 3, 'Captain'), (10, 4, 'First Officer'),
(11, 5, 'Captain'), (11, 2, 'First Officer'), (11, 9, 'Reserve'),
(12, 9, 'Captain'), (12, 8, 'First Officer'), (12, 1, 'Reserve'),
(13, 6, 'Captain'), (13, 7, 'First Officer'), (13, 5, 'Reserve'),
(14, 1, 'Captain'), (14, 2, 'First Officer'),
(15, 3, 'Captain'), (15, 4, 'First Officer'), (15, 5, 'Reserve'),
(16, 9, 'Captain'), (16, 8, 'First Officer'),
(17, 6, 'Captain'), (17, 7, 'First Officer'),
(18, 1, 'Captain'), (18, 2, 'First Officer');
