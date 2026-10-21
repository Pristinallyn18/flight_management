import sqlite3

#Option Lists
FLIGHT_STATUS = {
    "1" : "Scheduled",
    "2" : "Delayed",
    "3" : "Cancelled",
    "4" : "Rescheduled"
}

EMPLOYMENT_STATUS = {
    "1" : "Active",
    "2" : "On leave",
    "3" : "Retired"
}

FLIGHT_ROLE = {
    "1" : "Captain",
    "2" : "First Officer",
    "3" : "Reserve"
}


# Database helpers
def get_connection():
    conn = sqlite3.connect('flights.db')
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def fetch_results(query, values=()): 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    results = cursor.fetchall()
    conn.close()
    return results

def print_results(rows): 
    if not rows:
        print("No results found.")
        return
    for row in rows:
        print(row)
    input("\nPress Enter to continue...")

def run_change(query, values=()): 
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        count = cursor.rowcount
        return count
    finally:
        conn.close()

def choose_option(options):
    for key, value in options.items():
        print(key, value)
    choice = input("Select an option: ")
    return options.get(choice)

# Main Menu
def main_menu():
    while True:
        print('\n=== MAIN MENU ===')
        print('1 Flight')
        print('2 Destination')
        print('3 Pilots')
        print('4 Summaries')
        print('0 Exit')
        user_input = input('Select a number from the options: ')
        if user_input == '1':
            flight_menu()
        elif user_input == '2':
            destination_menu()
        elif user_input == '3':
            pilots_menu()
        elif user_input == '4':
            summaries_menu()
        elif user_input == '0':
            print('Goodbye')
            break
        else:
            print('Invalid input. Please try again')


# Flights Menu
def flight_menu():
    while True:
        print('\n=== FLIGHTS MENU ===')
        print('1 View all flights')
        print('2 View flights by destination')
        print('3 View flights by status')
        print('4 View flights by departure date')
        print('5 View flights by destination and status')
        print('6 Add a new flight')
        print('7 Change departure date or time')
        print('8 Change flight status')
        print('0 Back')
        user_input = input('Select a number from the options: ')
        if user_input == '1':
            view_all_flights()
        elif user_input == '2':
            view_flights_by_destination()
        elif user_input == '3':
            view_flights_by_status()
        elif user_input == '4':
            view_flights_by_departure_date()
        elif user_input == '5':
            view_flights_by_destination_and_status()
        elif user_input == '6':
            add_new_flight()
        elif user_input == '7':
            change_departure_date_or_time()
        elif user_input == '8':
            change_flight_status()
        elif user_input == '0':
            break
        else:
            print('Invalid input. Please try again')

# Destinations Menu
def destination_menu():
    while True:
        print('\n=== DESTINATIONS MENU ===')
        print('1 View all destinations')
        print('2 Update a destination')
        print('0 Back')
        user_input = input('Select a number from the options: ')
        if user_input == '1':
            view_all_destinations()
        elif user_input == '2':
            update_destination()
        elif user_input == '0':
            break
        else:
            print('Invalid input. Please try again')

# Pilots Menu
def pilots_menu():
    while True:
        print('\n=== PILOTS MENU ===')
        print('1 View active pilots')
        print('2 Assign a pilot to a flight')
        print('3 View a pilot schedule')
        print('4 View the crew of a flight')
        print('5 Remove a pilot from a flight')
        print('6 View pilots by employment status')
        print('0 Back')
        user_input = input('Select a number from the options: ')
        if user_input == '1':
            view_active_pilots()
        elif user_input == '2':
            assign_pilot_to_flight()
        elif user_input == '3':
            view_pilot_schedule()
        elif user_input == '4':
            view_flight_crew()
        elif user_input == '5':
            remove_pilot_from_flight()
        elif user_input == '6':
            view_pilots_by_employment_status()
        elif user_input == '0':
            break
        else:
            print('Invalid input. Please try again')

# Summaries Menu
def summaries_menu():
    while True:
        print('\n=== SUMMARY MENU ===')
        print('1 Flights per destination')
        print('2 Flights per pilot')
        print('0 Back')
        user_input = input('Select a number from the options: ')
        if user_input == '1':
            flights_per_destination()
        elif user_input == '2':
            flights_per_pilot()
        elif user_input == '0':
            break
        else:
            print('Invalid input. Please try again')

# Flight functions

# F1 - View all flights
def view_all_flights():
    query = """
        SELECT flight_id, flight_number, Destination.country, Destination.city, Flights.schedule_date, Flights.schedule_time, Flights.status
        FROM Flights
        JOIN Destination ON Flights.destination_id = Destination.destination_id
        ORDER BY flight_id
    """
    rows = fetch_results(query)
    print_results(rows)

# F2 - View flights by destination
def view_flights_by_destination():
    country = input("Enter country: ")
    query = """
        SELECT flight_id, flight_number, Destination.country, Destination.city, Flights.schedule_date, Flights.schedule_time, Flights.status
        FROM Flights
        JOIN Destination ON Flights.destination_id = Destination.destination_id
        WHERE Destination.country = ?
        ORDER BY Destination.city;
    """
    rows = fetch_results(query, (country,))
    print_results(rows)

# F3 - View flights by status
def view_flights_by_status():
    status = choose_option(FLIGHT_STATUS)

    if status is None:
        print("Invalid choice")
        return
    query = """
        SELECT flight_id, flight_number, Destination.country, Destination.city, Flights.schedule_date, Flights.schedule_time, Flights.status
        FROM Flights
        JOIN Destination ON Flights.destination_id = Destination.destination_id
        WHERE Flights.status = ?
        ORDER BY Flights.schedule_date;
    """
    rows = fetch_results(query, (status,))
    print_results(rows)

# F4 - View flights by departure date
def view_flights_by_departure_date():
    departure_date = input("Enter departure date (YYYY-MM-DD): ")
    query = """
        SELECT flight_id, flight_number, Destination.country, Destination.city, Flights.schedule_date, Flights.schedule_time, Flights.status
        FROM Flights
        JOIN Destination ON Flights.destination_id = Destination.destination_id
        WHERE Flights.schedule_date = ?
        ORDER BY Destination.country;
    """
    rows = fetch_results(query, (departure_date,))
    print_results(rows)

# F5 - View flights by destination and status
def view_flights_by_destination_and_status():
    city = input("Enter destination city: ")
    status = choose_option(FLIGHT_STATUS)

    if status is None:
        print("Invalid choice")
        return

    query = """
        SELECT flight_id, flight_number, Destination.country, Destination.city, Flights.schedule_date, Flights.schedule_time, Flights.status
        FROM Flights
        JOIN Destination ON Flights.destination_id = Destination.destination_id
        WHERE Destination.city = ? AND Flights.status = ?
        ORDER BY Flights.schedule_date
    """
    rows = fetch_results(query, (city, status))
    print_results(rows)


# F6 - Add a new flight
def add_new_flight():
    schedule_date = input("Enter departure date (YYYY-MM-DD): ")
    schedule_time = input("Enter departure time (HH:MM): ")
    departure_point = input("Enter departure point: ")
    aircraft_type = input("Enter aircraft type: ")
    flight_number = input("Enter flight number: ")
    destination_id = input("Enter destination ID: ")

    query = """
        INSERT INTO Flights (schedule_date, schedule_time, departure_point, aircraft_type, flight_number, destination_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    try:
        count = run_change(query, (schedule_date, schedule_time, departure_point, aircraft_type, flight_number, destination_id))
        if count == 0:
            print("No flight added")
        else:
            print("New flight added successfully")
    except sqlite3.IntegrityError as e:
        print("Insert failed:", e)

# F7 - Change a flight's departure date or time
def change_departure_date_or_time():
    flight_id = input("Enter flight ID: ")
    new_date = input("Enter new departure date (YYYY-MM-DD): ")
    new_time = input("Enter new departure time (HH:MM): ")

    query = """
        UPDATE Flights
        SET schedule_date = ?, schedule_time = ?
        WHERE flight_id = ?
    """
    try:
        count = run_change(query, (new_date, new_time, flight_id))
        if count == 0:
            print("No flight found with that ID")
        else:
            print("Flight departure date and time updated")
    except sqlite3.IntegrityError as e:
        print("Update failed:", e)

# F8 - Change a flight's status
def change_flight_status():
    flight_id = input("Enter flight ID: ")
    new_status = choose_option(FLIGHT_STATUS)

    if new_status is None:
        print("Invalid choice")
        return

    query = """
        UPDATE Flights
        SET status = ?
        WHERE flight_id = ?
    """
    try:
        count = run_change(query, (new_status, flight_id))
        if count == 0:
            print("No flight found with that ID")
        else:
            print("Flight status updated")
    except sqlite3.IntegrityError as e:
        print("Update failed:", e)



# Destination functions

# D1 - View all destinations
def view_all_destinations():
    query = """
        SELECT destination_id, country, city, airport_name, airport_code
        FROM Destination
        ORDER BY destination_id;
    """
    rows = fetch_results(query)
    print_results(rows)

# D2 - Update a destination
def update_destination():
    destination_id = input("Enter destination ID: ")
    new_city = input("Enter new city: ")
    new_airport_name = input("Enter new airport name: ")
    new_airport_code = input("Enter new airport code: ")

    query = """
        UPDATE Destination
        SET city = ?, airport_name = ?, airport_code = ?
        WHERE destination_id = ?
    """
    try:
        count = run_change(query, (new_city, new_airport_name, new_airport_code, destination_id))
        if count == 0:
            print("No destination found with that ID")
        else:
            print("Destination updated")
    except sqlite3.IntegrityError as e:
        print("Update failed:", e)


# Pilot functions

# P1 - View active pilots
def view_active_pilots():
    query = """
        SELECT pilot_id, pilot_name, license_registration
        FROM Pilots
        WHERE employment_status = 'Active'
        ORDER BY pilot_name;
    """
    rows = fetch_results(query)
    print_results(rows)

# P2 - Assign a pilot to a flight
def assign_pilot_to_flight():
    flight_id = input("Enter flight ID: ")
    pilot_id = input("Enter pilot ID: ")
    flight_role = choose_option(FLIGHT_ROLE)

    if flight_role is None:
        print("Invalid choice")
        return

    query = """
        INSERT INTO Flight_Assignment (flight_id, pilot_id, flight_role)
        VALUES (?, ?, ?)
    """
    try:
        count = run_change(query, (flight_id, pilot_id, flight_role))
        if count == 0:
            print("No pilot assignment added")
        else:
            print("Pilot assigned to flight")
    except sqlite3.IntegrityError as e:
        print("Assignment failed:", e)

# P3 - View a pilot's schedule
def view_pilot_schedule():
    pilot_name = input("Enter pilot name: ")
    query = """
        SELECT Pilots.pilot_id, Pilots.pilot_name, Flight_Assignment.flight_role, Flights.flight_number, Flights.schedule_date, Flights.schedule_time, Flights.departure_point
        FROM Pilots
        JOIN Flight_Assignment ON Flight_Assignment.pilot_id = Pilots.pilot_id
        JOIN Flights ON Flight_Assignment.flight_id = Flights.flight_id
        WHERE Pilots.pilot_name = ?
        ORDER BY Flights.schedule_date;
    """
    rows = fetch_results(query, (pilot_name,))
    print_results(rows)

# P4 - View the crew of a flight
def view_flight_crew():
    flight_id = input("Enter flight ID: ")
    query = """
        SELECT Flight_Assignment.flight_id, Flights.schedule_date, Flights.schedule_time, Pilots.pilot_name, Flight_Assignment.flight_role
        FROM Flight_Assignment
        JOIN Pilots ON Pilots.pilot_id = Flight_Assignment.pilot_id
        JOIN Flights ON Flights.flight_id = Flight_Assignment.flight_id
        WHERE Flight_Assignment.flight_id = ?
        ORDER BY Flight_Assignment.flight_role;
    """
    rows = fetch_results(query, (flight_id,))
    print_results(rows)


# P5 - Remove a pilot from a flight
def remove_pilot_from_flight():
    flight_id = input("Enter flight ID: ")
    pilot_id = input("Enter pilot ID: ")

    query = """
        DELETE FROM Flight_Assignment
        WHERE flight_id = ? AND pilot_id = ?
    """
    try:
        count = run_change(query, (flight_id, pilot_id))
        if count == 0:
            print("No pilot assignment found with those IDs")
        else:
            print("Pilot removed from flight")
    except sqlite3.IntegrityError as e:
        print("Removal failed:", e)

# P6 - View pilots by employment status
def view_pilots_by_employment_status():
    employment_status = choose_option(EMPLOYMENT_STATUS)
    if employment_status is None:
        print("Invalid choice")
        return
    
    query = """
        SELECT pilot_id, pilot_name, license_registration, employment_status
        FROM Pilots
        WHERE employment_status = ?
        ORDER BY pilot_name;
    """
    rows = fetch_results(query, (employment_status,))
    print_results(rows)


# Summary functions

# S1 - Number of flights per destination
def flights_per_destination():
    query = """
        SELECT Destination.country, Destination.city, COUNT(Flights.destination_id) AS total_flights
        FROM Destination
        LEFT JOIN Flights ON Destination.destination_id = Flights.destination_id
        GROUP BY Destination.destination_id
        ORDER BY total_flights DESC;
    """
    rows = fetch_results(query)
    print_results(rows)

# S2 - Number of flights per pilot
def flights_per_pilot():
    query = """
        SELECT Pilots.pilot_name, COUNT(Flight_Assignment.pilot_id) AS total_flights
        FROM Pilots
        LEFT JOIN Flight_Assignment ON Pilots.pilot_id = Flight_Assignment.pilot_id
        GROUP BY Pilots.pilot_id
        ORDER BY total_flights DESC;
    """
    rows = fetch_results(query)
    print_results(rows)

if __name__ == "__main__":
    main_menu()