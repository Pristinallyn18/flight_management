import sqlite3

def main_menu():
    while True:
        print('1 Flight')
        print('2 Destination')
        print('3 Pilots')
        print('4 Summaries')
        print('0 Exit')
        user_input = input('Select a number from the options:')
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



def flight_menu():
    pass

def destination_menu():
    pass

def pilots_menu():
    pass

def summaries_menu():
    pass

if __name__ == "__main__":
    main_menu()