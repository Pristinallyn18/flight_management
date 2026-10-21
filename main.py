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
    pass

def view_flights_by_status():
    pass

def view_flights_by_departure_date():
    pass

def view_flights_by_destination_and_status():
    pass

def add_new_flight():
    pass

def change_departure_date_or_time():
    pass

def change_flight_status():
    pass


# Destination functions

def view_all_destinations():
    pass

def update_destination():
    pass


# Pilot functions

def view_active_pilots():
    pass

def assign_pilot_to_flight():
    pass

def view_pilot_schedule():
    pass

def view_flight_crew():
    pass

def remove_pilot_from_flight():
    pass

def view_pilots_by_employment_status():
    pass


# Summary functions

def flights_per_destination():
    pass

def flights_per_pilot():
    pass

if __name__ == "__main__":
    main_menu()