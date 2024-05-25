'''@Author: Sheikh jainab

@Date: 2024-15-05 

@Last Modified by: Author Name

@Last Modified time: 2024-15-05

@Title : Address book problem . 
'''
class CreateContact:
    def __init__(self):
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.address = input("Enter your address: ")
        self.email = input("Enter your email id: ")
        self.phone = input("Enter your phone number: ")
        self.city = input("Enter your city name: ")
        self.state = input("Enter your state name: ")
        self.zip_code = input("Enter your area zip code: ")

    def display(self):
        print("Contact Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Address: {self.address}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"ZIP Code: {self.zip_code}")
        print(f"Phone Number: {self.phone}")
        print(f"Email: {self.email}")


class AddContacts:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found in the address book.")
        else:
            for contact in self.contacts:
                contact.display()
                print()

    def find_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                return contact
        return None


class EditContact:
    def __init__(self):
        pass

    def edit_contact(self, address_book):
        first_name = input("Enter the first name : ")
        contact = address_book.find_contact(first_name)
        if contact:
            contact.phone = input("Enter new phone number: ")
            contact.email = input("Enter new email: ")
            print("Contact updated successfully.")
        else:
            print("Contact not found.")


class DeleteDetails:
    def __init__(self):
        pass

    def delete_contact(self, address_book):
        first_name = input("Enter the first name : ")
        contact = address_book.find_contact(first_name)
        if contact:
            address_book.contacts.remove(contact)
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")


def main():
    address_book = AddContacts()  # Instantiate AddContacts object
    edit_contact = EditContact()  # Instantiate EditContact object
    delete_contact = DeleteDetails()  # Instantiate DeleteDetails object

    while True:
        print("\n____________WELCOME TO ADDRESS BOOK____________________")
        print("1. Add New Contact")
        print("2. Display all contacts")
        print("3. Edit contact")
        print("4. Delete contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            contact = CreateContact()  # Create new contact
            address_book.add_contact(contact)  # Add contact to address book
            print("Contact added successfully.")

        elif choice == '2':
            # Display all contacts
            address_book.display_contacts()

        elif choice == '3':
            # Edit existing contact
            edit_contact.edit_contact(address_book)

        elif choice == '4':
            # Delete contact
            delete_contact.delete_contact(address_book)

        elif choice == '5':
            print("Exiting the Address Book Program.")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()