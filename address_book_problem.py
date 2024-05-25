# this calss is for taking input from user for address book
'''Ability to create a Contacts in Address Book with
first and last names, address, city, state, zip, phone number and email '''
class CreateContact:
    def __init__(self):
        self.first_name = input("Enter your first name : ")
        self.last_name = input("Enter your last name : ")
        self.address = input("Enter your address : ")
        self.email = input("Enter your email id : ")
        self.phone = input("Enter your Phone number : ")
        self.city = input("Enter your city name : ")
        self.state = input("Enter your state name :")
        self.zip_code = input("Enter your area zip code : ")
    # function to display input
    def display(self):
        print("Contact Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Address: {self.address}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"ZIP Code: {self.zip_code}")
        print(f"Phone Number: {self.phone}")
        print(f"Email: {self.email}")


'''
Use case 2 : Ability to add a new Contact to Address Book Use Console to add person details from 
AddressBookMain class Use Object Oriented Concepts to manage 
relationship between AddressBook and Contact 
Person
'''
class AddContacts:
    def __init__(self):
        self.contacts = []

    def add_contacts(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found in the address book.")
        else:
            for contact in self.contacts:
                contact.display()
                print()
                
    def find_contact(self,first_name,last_name):
        for index, contact in enumerate(self.contacts):
            if first_name.lower() == contact.first_name.lower() and last_name.lower() == contact.last_name.lower():
                return index
        return None
            
                
        
''' Use Case 3:
Ability to edit existing contact person using their name
'''
class EditContact:
    
    def __init__(self):
        pass
    def edit_contact(self,contacts):
        first_name = input("Enter your first name : ")
        last_name = input("Enter your last name : ")
        email = input("Enter your email id : ")
        phone = input("Enter your Phone number : ")
        
        for contact in contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                contact.phone = phone
                contact.email = email
                
                print("Contact updated successfully.")
                return

        print("Contact not found.")
        
                  
def main():
    address_book = AddContacts()  # Instantiate AddContacts object
    edit_contact = EditContact()  # Instantiate EditContact objec

    while True:
        print("____________WELCOME TO ADDRESS BOOK____________________")
        print("1. Add New Contact")
        print("2. Display all contacts")
        print("3. Edit contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            contact = CreateContact()  # Create new contact
            address_book.add_contacts(contact)  # Add contact to address book
            print("Contact added successfully.")

        elif choice == '2':
            # Display all contacts
            address_book.display_contacts()  

        elif choice == '3':
            # Edit existing contact
            edit_contact.edit_contact(address_book.contacts)  

        elif choice == '4':
            print("Exiting the Address Book Program. Goodbye!")
            break

if __name__ == "__main__":
    main()