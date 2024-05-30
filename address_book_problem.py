
'''@Author: Sheikh jainab

@Date: 2024-24-05 

@Last Modified by: Author Name

@Last Modified time: 2024-27-05

@Title: Address book problem

'''
import json
import csv
"""
UC 1-4: Basic functionalities such as adding, editing, and deleting contacts in the address book.
UC 5: Adding support for multiple address books.
UC 6: Implementing duplicate entry checks.
UC 7: Searching for a person in a city or state across multiple address books.
UC 8: Viewing persons by city or state and maintaining dictionaries for efficient lookup.
UC 9: Getting the count of contact persons by city or state.
UC 10: Sorting entries alphabetically by person's name.
UC 11: Sorting entries by city, state, or zip code.
UC 12: Reading from and writing to a file using Java file I/O.
UC 13: Reading from and writing to a CSV file using the OpenCSV library.
UC 14: Reading from and writing to a JSON file using the GSON library.

"""

class AddressBookProblem:
    """Ability to create a Contacts in Address Book with first and last names, address, 
    city, state, zip, phone number and email"""

    def __init__(self):
        self.contacts = []

    def create_contact(self, contact=None):
        if contact is None:
            contact = {
                "first_name": input("Enter your first name: "),
                "last_name": input("Enter your last name: "),
                "address": input("Enter your address: "),
                "city": input("Enter your city name: "),
                "state": input("Enter your state: "),
                "zip": input("Enter your zip code: "),
                "phone_number": input("Enter your phone number: "),
                "email": input("Enter your email: ")
            }
            self.contacts.append(contact)
            print("\nThank you for entering details")
        else:
            # Reuse existing contact information for editing
            contact["address"] = input(f"Enter new address [{contact['address']}]: ") or contact["address"]
            contact["city"] = input(f"Enter new city [{contact['city']}]: ") or contact["city"]
            contact["state"] = input(f"Enter new state [{contact['state']}]: ") or contact["state"]
            contact["zip"] = input(f"Enter new zip code [{contact['zip']}]: ") or contact["zip"]
            contact["phone_number"] = input(f" Enter new phone number [{contact['phone_number']}]: ") or contact["phone_number"]
            contact["email"] = input(f"Enter new email [{contact['email']}]: ") or contact["email"]
            print("\nContact updated")

    def display_contact(self):
        if not self.contacts:
            print("No contact is present")
        else:
            for contact in self.contacts:
                print(f"Name: {contact['first_name']} {contact['last_name']}")
                print(f"Address: {contact['address']}")
                print(f"City: {contact['city']}")
                print(f"State: {contact['state']}")
                print(f"Zip Code: {contact['zip']}")
                print(f"Phone Number: {contact['phone_number']}")
                print(f"Email: {contact['email']}\n")

    def edit_contact(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        for contact in self.contacts:
            if contact["first_name"].lower() == first_name.lower() and contact["last_name"].lower() == last_name.lower():
                self.create_contact(contact)
                return
        print("No contact found")

    def delete_contact(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        for contact in self.contacts:
            if contact["first_name"].lower() == first_name.lower() and contact["last_name"].lower() == last_name.lower():
                self.contacts.remove(contact)
                print("Contact removed")
                return
        print("No contact found")

    def search_city(self):
        city = input("Enter city name: ").strip()
        found = False
        for contact in self.contacts:
            if contact["city"].lower() == city.lower():
                print(contact)
                found = True
        if not found:
            print("No contact is present")

    def view_by_city(self):
        city = input("Enter city name: ").strip()
        found = False
        for contact in self.contacts:
            if contact["city"].lower() == city.lower():
                print(f"Yes, there is a person in this {city}.")
                found = True
        if not found:
            print("No person is present")

    def count_person(self):
        count = 0
        city = input("Enter name of your city: ").strip()
        for c in self.contacts:
            if c["city"].lower() == city.lower():
                count += 1
        print(f"Total count: {count}")
        return count

    def sort_name(self):
        sorted_contacts = sorted(self.contacts, key=lambda x: x["first_name"].lower())
        return sorted_contacts

    def sort_by_city(self):
        sorted_contacts = sorted(self.contacts, key=lambda x: (x["city"].lower(), x["state"].lower(), x["zip"]))
        return sorted_contacts
    #  use case 13

    def read_file(self, filename):
        try:
            with open(filename, "r") as f:
                file_handler = f.read()
                print(file_handler)
        except FileNotFoundError:
            print("File not found.")

    def write_file(self, filename):
        with open(filename, "w") as f:
            f.write("This is some data. Writing.")
    
    def read_json(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.contacts = data.get('contacts', [])
                print("Address book loaded from JSON file successfully.")
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")

    def write_json(self, filename):
        data = {'contacts': self.contacts}
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
                print("Address book written to JSON file successfully.")
        except IOError:
            print("Error writing to file.")
            
            
    def read_csv(self, filename):
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                self.contacts = list(reader)
                print("Address book loaded from CSV file successfully.")
        except FileNotFoundError:
            print("File not found.")
        except csv.Error:
            print("Error reading CSV file.")

    def write_csv(self, filename):
        fieldnames = self.contacts[0].keys() if self.contacts else []
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.contacts)
                print("Address book written to CSV file successfully.")
        except IOError:
            print("Error writing to file.")


class NewAddressBook:
    def __init__(self):
        self.books = {}

    def new_book(self):
        book_name = input("Please enter the name of your book: ")
        if book_name in self.books:
            print("Book already exists")
        else:
            self.books[book_name] = AddressBookProblem()
            print("New book created")

    def get_book(self, book_name):
        return self.books.get(book_name, None)

    def duplicate_entry(self, book, contact):
        first_name = contact["first_name"]
        last_name = contact["last_name"]
        for existing_contact in book.contacts:
            if existing_contact["first_name"].lower() == first_name.lower() and existing_contact["last_name"].lower() == last_name.lower():
                print("Contact with this name already exists.")
                return True
        return False

    def display_books(self):
        if not self.books:
            print("No books are present")
        else:
            for book_name in self.books:
                print(book_name)



def main():
    address_book_system = AddressBookProblem()
    new_address_book = NewAddressBook()
    

    print("\n****_____WELCOME TO ADDRESS BOOK PROBLEM_____*****")
    print("\n")
    while True:
        print("\n OPTIONS :- ")
        print("1. EXIT")
        print("2. ADD NEW CONTACT")
        print("3. DISPLAY CONTACT")
        print("4. EDIT CONTACT")
        print("5. DELETE CONTACT")
        print("6. ADD NEW ADDRESS BOOK")
        print("7. ADD DETAILS TO ADDRESS BOOK")
        print("8. SEARCH BY CITY")
        print("9. COUNT PERSON")
        print("10. PRINT CONTACT IN SORTED ORDER")
        print("11. SORTED BY CITY NAME")
        print("12. SORT CITY NAME")
        print("13. I/O File")
        print("14. json")
        print("15. csv file")
        choice = input("Enter your choice in numbers: ")
        if choice == '1':
            print("Exiting the program")
            break
        elif choice == '2':
            print("\nAdd your details:")
            address_book_system.create_contact()
        elif choice == '3':
            address_book_system.display_contact()
        elif choice == '4':
            address_book_system.edit_contact()
        elif choice == '5':
            address_book_system.delete_contact()
        elif choice == '6':
            new_address_book.new_book()
        elif choice == '7':
            new_address_book.display_books()
            book_name = input("Enter the book name you want to use: ")
            book = new_address_book.get_book(book_name)
            if book:
                while True:
                    print("\n1. EXIT")
                    print("2. ADD NEW CONTACT")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == '1':
                        print("Exiting book menu")
                        break
                    elif sub_choice == '2':
                        print("Enter your address book details:")
                        book.create_contact()
                    else:
                        print("INVALID INPUT")
            else:
                print("Book not found")
                
        elif choice == '8':
            address_book_system.search_city()
            
        elif choice == '9':
            address_book_system.count_person()
            
        elif choice == '10':
            sorted_contacts = address_book_system.sort_name()
            print("Sorted contacts:")
            for contact in sorted_contacts:
                print(contact)
                
        elif choice == '11':
            sorted_contacts = address_book_system.sort_by_city()
            print("Sorted contacts:")
            for contact in sorted_contacts:
                print(contact)
                
        elif choice == '12':
            address_book_system.sort_by_city()
            
        elif choice == '13':
            while True:
                print("1.read file:")
                print("2.write file:")
                print("3.exit :")
                sub_choice = input("enter your choice")

                if sub_choice == '1':
                    print("reading file ")
                
                    address_book_system.read_file("address_book_system")
                elif sub_choice == '2':
                    print("write in file")
                    address_book_system.write_file("address_book_system")
                elif sub_choice == '3':
                    print("exiting")
                    break
                
        elif choice == '14':
            address_book_system.read_json("address_book_system")
            address_book_system.write_json("address_book_system")
            
        elif choice == '15':
            address_book_system.read_csv("address_book_system")
            address_book_system.write_csv("address_book_system")
            
        else:
            print("\nINVALID CHOICE, TRY AGAIN")


if __name__ == "__main__":
    main()