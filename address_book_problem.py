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
    def create_contact(self,contact = None):
        if contact is None:
          
            contact = {}
            contact["first_name"] = input("Enter your first name :"),
            contact["last_name"] = input("Enter your last name: "),
            contact["address"] = input("Enter your address: "),
            contact["city"] = input("Enter your city nmae : "),
            contact["state"] = input("Enter your State : "),
            contact["zip"] = input("Enter your zip code : "),
            contact["phone_number"] = input("Enter your phone Number : "),
            contact["email"] = input("Enter your email : ")
        
            self.contacts.append(contact)
            print("\n Thankyou for entering details")
        else:
            # Reuse existing contact information for editing
            contact["address"] = input(f"Enter new address [{contact['address']}]: ") or contact["address"]
            contact["city"] = input(f"Enter new city [{contact['city']}]: ") or contact["city"]
            contact["state"] = input(f"Enter new state [{contact['state']}]: ") or contact["state"]
            contact["zip"] = input(f"Enter new zip code [{contact['zip']}]: ") or contact["zip"]
            contact["phone_number"] = input(f"Enter new phone number [{contact['phone_number']}]: ") or contact["phone_number"]
            contact["email"] = input(f"Enter new email [{contact['email']}]: ") or contact["email"]
            print("\nContact updated")

        
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
    def edit_contact(self):
        first_name = input("Enter your first name : ")
        last_name = input("enter your last name:  ")
        for contact in self.contacts:
            if contact["first_name"].lower() == first_name.lower() and contact["last_name"].lower() == last_name.lower():
                self.create_contact(contact)
                print("\ncontact updated")
                return
            else:
                print("no contact found ")
                 
        
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
        print("4.EDIT CONTACT")
        choice = input("Enter your choice in numbers : ")
        if choice == '1':
            print("Exiting the program")
            break
        elif choice == '2':
            print("\n Add your details :")
            address_book_system.create_contact()
        elif choice == '3':
            address_book_system.display_contact()
        elif choice == '4':
            address_book_system.edit_contact()
        else:
            print("\n INVALID CHOICE, TRY AGAIN ")
        
    
if __name__ =="__main__":
    main()