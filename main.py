import sqlite3

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

def view_all_flights():
    query = """
        SELECT flight_id, flight_number, Destination.country, Destination.city, Flights.schedule_date, Flights.schedule_time, Flights.status
        FROM Flights
        JOIN Destination ON Flights.destination_id = Destination.destination_id
        ORDER BY flight_id
    """
    rows = fetch_results(query)
    print_results(rows)

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

def view_flights_by_status():
    status = input("Enter flight status: ")
    query = """
        SELECT flight_id, flight_number, Destination.country, Destination.city, Flights.schedule_date, Flights.schedule_time, Flights.status
        FROM Flights
        JOIN Destination ON Flights.destination_id = Destination.destination_id
        WHERE Flights.status = ?
        ORDER BY Flights.schedule_date;
    """
    rows = fetch_results(query, (status,))
    print_results(rows)

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

def view_flights_by_destination_and_status():
    city = input("Enter destination city: ")
    status = input("Enter flight status: ")
    query = """
        SELECT flight_id, flight_number, Destination.country, Destination.city, Flights.schedule_date, Flights.schedule_time, Flights.status
        FROM Flights
        JOIN Destination ON Flights.destination_id = Destination.destination_id
        WHERE Destination.city = ? AND Flights.status = ?
        ORDER BY Flights.schedule_date;
    """
    rows = fetch_results(query, (city, status))
    print_results(rows)

def add_new_flight():
    pass

def change_departure_date_or_time():
    pass

def change_flight_status():
    pass


# Destination functions

def view_all_destinations():
    query = """
        SELECT destination_id, country, city, airport_name, airport_code
        FROM Destination
        ORDER BY destination_id;
    """
    rows = fetch_results(query)
    print_results(rows)

def update_destination():
    pass


# Pilot functions

def view_active_pilots():
    query = """
        SELECT pilot_id, pilot_name, license_registration
        FROM Pilots
        WHERE employment_status = 'Active'
        ORDER BY pilot_name;
    """
    rows = fetch_results(query)
    print_results(rows)

def assign_pilot_to_flight():
    pass

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

def remove_pilot_from_flight():
    pass

def view_pilots_by_employment_status():
    employment_status = input("Enter employment status: ")
    query = """
        SELECT pilot_id, pilot_name, license_registration, employment_status
        FROM Pilots
        WHERE employment_status = ?
        ORDER BY pilot_name;
    """
    rows = fetch_results(query, (employment_status,))
    print_results(rows)


# Summary functions

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