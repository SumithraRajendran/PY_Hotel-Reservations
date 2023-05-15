import datetime

# List to hold the available rooms
available_rooms = [101, 102, 103, 104, 105]

# Dictionary to hold the booked rooms and their details
booked_rooms = {}

# Function to book a room for a specific date
def book_room(room_number, start_date, end_date, customer_name):
    if room_number not in available_rooms:
        print("Sorry, that room is not available.")
    else:
        available_rooms.remove(room_number)
        booked_rooms[room_number] = {
            'start_date': start_date,
            'end_date': end_date,
            'customer_name': customer_name
        }
        print(f"Room {room_number} has been booked for {customer_name} from {start_date} to {end_date}.")

# Function to book half of a room for a specific date
def book_half_room(room_number, start_date, end_date, customer_name):
    if room_number not in available_rooms:
        print("Sorry, that room is not available.")
    else:
        available_rooms.remove(room_number)
        booked_rooms[room_number] = {
            'start_date': start_date,
            'end_date': end_date,
            'customer_name_1': customer_name,
            'customer_name_2': None
        }
        print(f"Half of room {room_number} has been booked for {customer_name} from {start_date} to {end_date}.")

# Function to allot the other half of a room for a specific date
def allot_half_room(room_number, start_date, end_date, customer_name):
    if room_number not in booked_rooms:
        print("Sorry, that room is not booked.")
    elif booked_rooms[room_number].get('customer_name_2') is not None:
        print("Sorry, that half of the room is already booked.")
    else:
        booked_rooms[room_number]['customer_name_2'] = customer_name
        print(f"The other half of room {room_number} has been allotted to {customer_name} from {start_date} to {end_date}.")

# Function to book a room for a full day
def book_full_day(room_number, booking_date, customer_name):
    if room_number not in available_rooms:
        print("Sorry, that room is not available.")
    else:
        available_rooms.remove(room_number)
        booked_rooms[room_number] = {
            'start_date': booking_date,
            'end_date': booking_date + datetime.timedelta(days=1),
            'customer_name': customer_name
        }
        print(f"Room {room_number} has been booked for {customer_name} on {booking_date}.")

# Function to cancel a booked room
def cancel_room(room_number):
    if room_number not in booked_rooms:
        print("Sorry, that room is not booked.")
    else:
        available_rooms.append(room_number)
        del booked_rooms[room_number]
        print(f"Room {room_number} has been cancelled.")

# Function to calculate the extra pay for an overstayed room
def calculate_extra_pay(room_number, end_date):
    if room_number not in booked_rooms:
        print("Sorry, that room is not booked.")
    elif end_date < booked_rooms[room_number]['end_date']:
        print("Sorry, the end date cannot be before the original booking end date.")
    else:
        extra_days = (end_date - booked_rooms[room_number]['end_date']).days
        print("The extra payment has been done.")

# Book a full day for room 101 on May 13, 2023
book_full_day(101, datetime.date(2023, 5, 13), "John Doe")

# Book half of room 102 for John on May 14, 2023
book_half_room(102, datetime.date(2023, 5, 14), datetime.date(2023, 5, 15), "Priya")

# Allot the other half of room 102 to Jane on May 14, 2023
allot_half_room(102, datetime.date(2023, 5, 14), datetime.date(2023, 5, 15), "Gajalakshmi")

# Book room 103 for May 16, 2023 to May 18, 2023 for Jane
book_room(103, datetime.date(2023, 5, 16), datetime.date(2023, 5, 18), "Rajendran")

# Cancel room 104
cancel_room(104)

# Calculate extra pay for an overstayed room 101 until May 14, 2023
calculate_extra_pay(101, datetime.date(2023, 5, 15))