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


''''
Use case 2 : Ability to add a new Contact to Address Book Use Console to add person details from 
AddressBookMain class Use Object Oriented Concepts to manage 
relationship between AddressBook and Contact 
Person
'''
class AddContacts:
    def __init__(self):
        self.contacts = []
        
    def add_contacts(self,contact):
        self.contacts.append(contact)
    def contact_show(self):
        if not  self.contacts:
            print("Contat not found in address book")
        else:
            for contact in self.contacts:
                contact.display()
                print()
        
        
def main():
    new_contact = AddContacts()  # Instantiate AddContacts object

    while True:
        print("____________WELCOME TO ADDRESS BOOK____________________")
        print("1. Add New Contact")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
        #    for adding new contact 
            contact = CreateContact()
            new_contact.add_contacts(contact) # this is an instance of a class add contact
            print("Contact added ")
        elif choice == '2':
            break
            exit()            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()