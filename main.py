from utils.sql_functions import *
from email_validator import validate_email, EmailNotValidError
from tabulate import tabulate



def get_input():
    name = input("Enter the name: ")

    phone = input("Enter the phone number: ")
    while not phone.isdigit():
        phone = input("Enter the phone number: ")
        if phone.isdigit():
            break
        else:
            print("Enter a valid phone number!")

    address = input("Enter address (enter to leave blank): ")

    while True:
        email = input("Enter the email (enter to leave blank): ")
        if email != '':
            try:
                valid = validate_email(email)
                email = valid.email
                break

            except EmailNotValidError as e:
                print("Enter a Valid Email!")
        else:
            break

    return name, phone, address, email

while True:
    print("""
    (1) new contact
    (2) edit contact
    (3) delete contact
    (4) see all contacts
    (5) Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        name, phone, address, email = get_input()
        if email == '':
            email = None
        if address == '':
            address = None

        insert_data(name, int(phone), address, email)

    elif choice == "2":
        id = int(input("Enter the id of the contact: "))
        name, phone, address, email = get_input()

        if email == '':
            email = None
        if address == '':
            address = None

        update_data(id, name, int(phone), address, email)

    elif choice == "3":
        choice = input("D'you wanna delete all the entries: ")[:1]

        if choice == "y":
            delete_data(None)
        else:
            contact_id = int(input("Enter the id of the contact: "))
            delete_data(contact_id)

    elif choice == "4":
        categories = ["name", "phone", "address", "email", "id"]

        category = input("Enter category to search contacts for(Leave empty to see all): ").lower()

        if category == "":
            data = get_data()
            print(tabulate(data, headers=["ID", "Name", "Phone Number", "Address", "Email"]))
        elif category not in categories:
            print(f"Invalid Category! Possible Categories: {', '.join(categories)}")
        else:
            data = input(f"What do you wanna search for in {category} category: ")
            get_data(category, data)
            print(data)

    elif choice == "5":
        break

    elif choice == '':
        continue

    else:
        print("Invalid Choice")
        break