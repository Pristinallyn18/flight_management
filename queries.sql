-- QUERIES TO RETRIEVE FROM FLIGHTS TABLE

-- (1) View all flights using destination city

-- (2) View flights by destination

-- (3) View flights by status

-- (4) View flights by departure date

-- (5) View flights by destination and status

-- (6) Add a new flight

-- (7) Change a flight’s departure date or time

-- (8) Change a flight’s status


-- QUERIES TO RETRIEVE FROM PILOTS TABLE

-- (1) Selecting 'Active' pilots

SELECT pilot_id, pilot_name, license_registration
FROM Pilots
WHERE employment_status = 'Active'
ORDER BY pilot_name;

-- (2) Assign a pilot to a flight

-- (3) View a pilot’s schedule or assignment

-- (4) View the crew of a flight

-- (5) Remove a pilot from a flight

-- (6) View pilots with their current status


-- QUERIES TO RETRIEVE FROM DESTINATIONS

-- (1) View all destinations

-- (2) Update a destination’s details

-- SUMMARY VIEW

-- (1) Number of flights to each destination

-- (2) Number of flights per pilot



