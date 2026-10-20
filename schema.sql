PRAGMA foreign_keys = ON;

CREATE TABLE Destination (
destination_id INTEGER PRIMARY KEY, 
country TEXT NOT NULL,
city TEXT NOT NULL,
airport_name TEXT NOT NULL,
airport_code TEXT NOT NULL UNIQUE
);

CREATE TABLE Flights (
flight_id INTEGER PRIMARY KEY,
flight_number TEXT NOT NULL,
aircraft_type TEXT NOT NULL,
departure_point TEXT NOT NULL,
schedule_date TEXT NOT NULL,
schedule_time TEXT NOT NULL,
destination_id INTEGER,
status TEXT NOT NULL DEFAULT 'Scheduled'
CHECK (status IN ('Scheduled', 'Delayed', 'Cancelled', 'Rescheduled')),
FOREIGN KEY (destination_id) REFERENCES Destination(destination_id)
);

CREATE TABLE Pilots (
pilot_id INTEGER PRIMARY KEY,
pilot_name TEXT NOT NULL,
license_registration TEXT NOT NULL,
employment_status TEXT NOT NULL DEFAULT 'Active'
CHECK (employment_status IN ('Active', 'On leave', 'Retired'))
);

CREATE TABLE Flight_Assignment (
flight_id 
INTEGER,
pilot_id INTEGER,
flight_role TEXT NOT NULL
CHECK (flight_role IN ('Captain', 'First Officer', 'Reserve')),
PRIMARY KEY (flight_id, pilot_id),
FOREIGN KEY (flight_id) REFERENCES Flights(flight_id),
FOREIGN KEY (pilot_id) REFERENCES Pilots(pilot_id)
);