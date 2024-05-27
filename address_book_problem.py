'''@Author: Sheikh jainab

@Date: 2024-24-05 

@Last Modified by: Author Name

@Last Modified time: 2024- 27-05

@Title : Address book problem

'''
""""
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
    """"Ability to create a Contacts in Address Book with first and last names, address, 
    city, state, zip, phone number and email"""
    
    # for contact
    def __init__(self):
        self.contacts = []
    def create_contact(self):
        first_name = input("Enter your first name :")
        last_name = input("Enter your last name: ")
        address = input("Enter your address: ")
        city = input("Enter your city nmae : ")
        state = input("Enter your State : ")
        zip = input("Enter your zip code : ")
        phone_number = input("Enter your phone Number : ")
        email = input("Enter your email : ")
        contact = {
                "first_name": first_name,
                "last_name": last_name,
                "address": address,
                "city": city,
                "state": state,
                "zip": zip,
                "phone_number": phone_number,
                "email": email
            }
        self.contacts.append(contact)
        print("\n Thankyou for entering details")

        
    # for displaying contact    
    def display_contact(self):
        try:
            if not self.contact:
                print("No contact is present")
            else:
                for contact in self.contacts:
                    print(f"Name: {contact['first_name']} {contact['last_name']}")
                    print(f"Address: {contact['address']}")
                    print(f"City: {contact['city']}")
                    print(f"State: {contact['state']}")
                    print(f"Zip Code: {contact['zip_code']}")
                    print(f"Phone Number: {contact['phone_number']}")
                    print(f"Email: {contact['email']}\n")
        except Exception as e :
            print("An error occured ", e)
        
def main():
    address_book_system = AddressBookProblem()
    print("\n****_____WELCOME TO ADDRESS BOOK PROBLEM_____*****" )
    print("\n")
    # creating options
    while True:
        print("\n OPTIONS :- ")
        print("1.EXIT")        
        print("2.ADD NEW CONTACT")
        print("3.DISPLAY CONTACT ")
        choice = input("Enter your choice in numbers : ")
        if choice == '1':
            print("Exiting the program")
            break
        elif choice == '2':
            print("\n Add your details :")
            address_book_system.create_contact()
        elif choice == '3':
            address_book_system.display_contact()
        else:
            print("\n INVALID CHOICE, TRY AGAIN ")
        
    
if __name__ =="__main__":
    main()