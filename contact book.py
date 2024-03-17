class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contacts:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")

    def search_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)
        if found_contacts:
            print("Matching contacts:")
            for index, contact in enumerate(found_contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
        else:
            print("No matching contacts found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if name.lower() == contact.name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            contact_book.add_contact(contact)
        elif choice == '2':
            contact_book.display_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
