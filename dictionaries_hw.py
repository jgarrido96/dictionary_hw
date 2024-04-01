print('\n')
# 1. Real-World Python Dictionary Applications

# Restaurant Menu Update

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Soda": 0.99, "Beer": 4.99}


restaurant_menu["Main Course"].update({"Steak": 17.99})


del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)


# 2. Advanced Data Handling with Python

# Task 1: Hotel Room Booking Tracker

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

# username = input("Welcome to JDoggs Slee-Zzz Inn! Please provide a name for your Slee-Zzz experience. ")

def jdogg_inn():
    while True:
        user_input = input(f"\nWelcome {username}! What would you like to do today?\nTo book a room, type 'book'.\nTo check-out, type 'out'.\nTo check availability, type 'vacancy'.\nTo quit, type 'quit'.\n")
        if user_input == 'quit':
            break
        elif user_input == 'book':
            book_input = input("Room 101 is available! To book this room, type y/n or type 'return' to return to the main menu. ")
            if book_input == "return":
                continue
            elif book_input == 'y':
                hotel_rooms["101"].update({"status": "booked", "customer": username})
                print("You're now booked in room 101!")
            elif book_input == 'n':
                n_input = input("It might not be ethical, but we do have another room but someone else is staying in it.\n... If you want room 102, we can take care of the problem.\n Type 'y' to hire a hit. Type 'n' to just take room 101\n")
                if n_input == 'y':
                    print("\nA man named Vinny enters room 102. He leaves with a big rolled carpet.")
                    hotel_rooms["102"].update({"status": "booked", "customer": username})
                    print("You're now booked in room 102!")
        elif user_input == 'out':
            out_input = str(input("Which room would you like to check out of? "))
            if out_input == "101":
                hotel_rooms["101"].update({"status": "available", "customer": ""})
                print("You have successfully checked out of room 101!")
            elif out_input == "102":
                hotel_rooms["102"].update({"status": "available", "customer": ""})
                print("You have successfully checked out of room 102!")
            else:
                print("Sorry, we're like a really small Inn. We only have 2 rooms.")
        elif user_input == 'vacancy':
            print(hotel_rooms.items())
        else:
            print("Sorry! That's an invalid input!")

# jdogg_inn()

# Task 2: E-Commerce Product Search Feature


# def search_nested_dict(dictionary, value):
#     for k, v in dictionary.items():
#         if dictionary[k]['name'] == value:
#             return v
#     return None

# products = {
#     "1": {"name": "Laptop", "category": "Electronics", "price": 800},
#     "2": {"name": "Shirt", "category": "Clothing", "price": 20},
#     "3": {"name": "Shoe", "category": "Clothing", "price": 40},
#     "4": {"name": "Chair", "category": "Office", "price": 85}
# }
# while True:
#     value_to_search = input("Welcome to this super powerful search engine! Enter your search here! Type 'quit' to quit. ")
#     if value_to_search == 'quit':
#         break
#     result = search_nested_dict(products, value_to_search)
#     if result is not None:
#         print(f"Value for key '{value_to_search}': {result}")
#     else:
#         print(f"Search for '{value_to_search}' retuned no results.")


# 3. Python Programming Challenges for Customer Service Data Handling

# Task 1: Customer Service Ticets
print('\n')
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def tickets():
    while True:
        user_input = input("\nWelcome! What would you like to do today?\nTo display tickets type 'display'.\nTo update the status of your ticket type 'update'.\nTo open a new ticket, type 'open'.\nTo quit type 'quit'. ")
        if user_input == 'quit':
            break
        elif user_input == 'display':
            for ticket in service_tickets:
                print(f'{ticket}\t{service_tickets[ticket]["Customer"]}\t{service_tickets[ticket]["Status"]}\t{service_tickets[ticket]["Issue"]}')
        elif user_input == 'update':
            ticket_number = input("Please enter your ticket number: ")
            new_status = input("Enter new status: ")
            if ticket_number in service_tickets:
                service_tickets[ticket_number]["Status"] = new_status
        elif user_input == 'open':
            name_input = input("Please provide your name: ")
            issue_input = input("What seems to be the issue? ")
            new_key = (f"Ticket00{str(len(service_tickets)+1)}")
            service_tickets[new_key] = {"Customer": name_input, "Issue": issue_input, "Status": "open"}

# tickets()

# 4. Python Essentials for Business Analytics

# Task 1: Sales Data Cloning and Modification

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}
import copy

weekly_copy = copy.deepcopy(weekly_sales)

weekly_copy["Week 2"].update({"Electronics": 18000})
print(weekly_sales)
print("\n")
print(weekly_copy)