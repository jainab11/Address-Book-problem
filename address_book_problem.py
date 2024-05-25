'''@Author: Sheikh jainab

@Date: 2024-25-05 

@Last Modified by: Author Name

@Last Modified time: 2024-25-05

@Title : Address book problem
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
# add only unique name
    def unique_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                print("Contact already exists")
                return False
        return True
# add contacs
    def add_contact(self, contact):
        if self.unique_contact(contact.first_name, contact.last_name):
            self.contacts.append(contact)
            print("Contact added successfully.")
# display contcat
    def display_contacts(self):
        if not self.contacts:
            print("No contacts found in the address book.")
        else:
            for contact in self.contacts:
                contact.display()
                print()
#  find contact funtion to check if nam ei there or not to perfom oprtions
    def find_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                return contact
        return None

# add multiple address book
class MultipleAddressBook:
    def __init__(self):
        # using dictionary to store address book name as key and contacts as value
        self.address_books = {}

    def add_address_book(self, name):
        if name.lower() not in self.address_books:
            try:
                self.address_books[name.lower()] = AddContacts()
                print("Address book added successfully.")
            except:
                print("Address book already exists.")
        else:
            print("Address book with that name already exists.")

    def get_address_book(self, name):
        return self.address_books.get(name.lower())


class EditContact:
    def edit_contact(self, address_book):
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        contact = address_book.find_contact(first_name, last_name)
        if contact:
            contact.phone = input("Enter new phone number: ")
            contact.email = input("Enter new email: ")
            print("Contact updated successfully.")
        else:
            print("Contact not found.")


class DeleteDetails:
    def delete_contact(self, address_book):
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        contact = address_book.find_contact(first_name, last_name)
        if contact:
            address_book.contacts.remove(contact)
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")


def main():
    address_book_system = MultipleAddressBook()
    edit_contact = EditContact()
    delete_contact = DeleteDetails()

    while True:
        print("\n____________WELCOME TO ADDRESS BOOK SYSTEM____________________")
        print("1. Add New Address Book")
        print("2. Select Address Book")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name for the new address book: ")
            address_book_system.add_address_book(name)

        elif choice == '2':
            name = input("Enter the name of the address book: ")
            address_book = address_book_system.get_address_book(name)
            if address_book:
                while True:
                    print(f"\n____________{name.upper()} ADDRESS BOOK____________________")
                    print("1. Add New Contact")
                    print("2. Display all contacts")
                    print("3. Edit contact")
                    print("4. Delete contact")
                    print("5. Back to Main Menu")
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        contact = CreateContact()
                        address_book.add_contact(contact)

                    elif choice == '2':
                        address_book.display_contacts()

                    elif choice == '3':
                        edit_contact.edit_contact(address_book)

                    elif choice == '4':
                        delete_contact.delete_contact(address_book)

                    elif choice == '5':
                        break

                    else:
                        print("Invalid choice.")

            else:
                print("Address book not found.")

        elif choice == '3':
            print("Exiting the Address Book System.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
