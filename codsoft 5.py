contacts = {}

def add_contact():
    name = input("Enter name: ").strip().title()
    phone = input("Enter phone number (10 digits): ").strip()
    while not (phone.isdigit() and len(phone) == 10):
        print("Invalid phone number. It should be exactly 10 digits.")
        phone = input("Enter phone number (10 digits): ").strip()
    email = input("Enter email (must contain '@' and '.com'): ").strip()
    while "@" not in email or not email.endswith(".com"):
        print("Invalid email. It should contain '@' and end with '.com'.")
        email = input("Enter email (must contain '@' and '.com'): ").strip()
    address = input("Enter address: ").strip()
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"Contact for {name} added.\n")

def view_contacts():
    if contacts:
        for name, details in contacts.items():
            print(f"Name: {name},\nPhone: {details['Phone']},\nEmail: {details['Email']},\nAddress: {details['Address']}")
    else:
        print("No contacts found.")
    print()

def search_contact():
    search_name = input("Enter name to search: ").strip().title()
    if search_name in contacts:
        details = contacts[search_name]
        print(f"Found: {search_name} - Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
    else:
        print("Contact not found.")
    print()

def delete_contact():
    name = input("Enter name to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted.\n")
    else:
        print("Contact not found.\n")

while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("select the number from the option : ").strip()
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("bye")
        break
    else:
        print("Invalid option.")


