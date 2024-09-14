contacts = {}

def add():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully!\n")

def view():
    if contacts:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}")
    else:
        print("No contacts available.\n")

def search():
    search = input("Enter name or phone number to search: ")
    for name, info in contacts.items():
        if search in name or search in info['phone']:
            print(f"\nFound Contact - Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}\n")
            return
    print("Contact not found.\n")

def update():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")

        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' updated successfully!\n")
    else:
        print(f"No contact found with the name '{name}'.\n")

def delete():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!\n")
    else:
        print(f"No contact found with the name '{name}'.\n")

def main():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add()
        elif choice == '2':
            view()
        elif choice == '3':
            search()
        elif choice == '4':
            update()
        elif choice == '5':
            delete()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
