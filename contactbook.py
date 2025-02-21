contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print(f"Contact '{name}' added.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for i, contact in enumerate(contacts):
            print(f"{i + 1}. {contact['name']} - {contact['phone']}")

def search_contact():
    search = input("Enter name or phone number to search: ").lower()
    found_contacts = [contact for contact in contacts if search in contact["name"].lower() or search in contact["phone"]]
    
    if not found_contacts:
        print("No contacts found.")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact():
    search = input("Enter name or phone number of the contact to update: ").lower()
    found_contacts = [contact for contact in contacts if search in contact["name"].lower() or search in contact["phone"]]
    
    if not found_contacts:
        print("No contacts found.")
    else:
        contact = found_contacts[0]
        print(f"Updating contact: {contact['name']}")
        contact["name"] = input(f"Enter new name (current: {contact['name']}): ") or contact["name"]
        contact["phone"] = input(f"Enter new phone number (current: {contact['phone']}): ") or contact["phone"]
        contact["email"] = input(f"Enter new email (current: {contact['email']}): ") or contact["email"]
        contact["address"] = input(f"Enter new address (current: {contact['address']}): ") or contact["address"]
        print(f"Contact '{contact['name']}' updated.")

def delete_contact():
    search = input("Enter name or phone number of the contact to delete: ").lower()
    found_contacts = [contact for contact in contacts if search in contact["name"].lower() or search in contact["phone"]]
    
    if not found_contacts:
        print("No contacts found.")
    else:
        contact = found_contacts[0]
        contacts.remove(contact)
        print(f"Contact '{contact['name']}' deleted.")

def main():
    print("Welcome to the Contact Manager!")
    
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
