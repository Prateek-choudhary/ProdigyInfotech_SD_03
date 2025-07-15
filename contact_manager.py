import json
import os


CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("✅ Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} | {contact['phone']} | {contact['email']}")


def edit_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to edit: ")) - 1
        if 0 <= index < len(contacts):
            contacts[index]['name'] = input("Enter new name: ")
            contacts[index]['phone'] = input("Enter new phone: ")
            contacts[index]['email'] = input("Enter new email: ")
            print("✏️ Contact updated.")
        else:
            print("❌ Invalid contact number.")
    except ValueError:
        print("❌ Invalid input.")


def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"🗑️ Deleted contact: {removed['name']}")
        else:
            print("❌ Invalid contact number.")
    except ValueError:
        print("❌ Invalid input.")

def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("💾 Contacts saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
