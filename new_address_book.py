'''@Author: Sheikh jainab

@Date: 2024-24-05 

@Last Modified by: Author Name

@Last Modified time: 2024- 25-05

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
    def create_contact(self):
        self.first_name = input("Enter your first name :")
        self.last_name = input("Enter your last name: ")
        self.address = input("Enter your address: ")
        self.city = input("Enter your city nmae : ")
        self.state = input("Enter your State : ")
        self.zip = input("Enter your zip code : ")
        self.phone_number = input("Enter your phone Number : ")
        self.email = input("Enter your email : ")
        print("\n Thankyou for entering details")
def main():
    address_book_system = AddressBookProblem()
    print("\n****_____WELCOME TO ADDRESS BOOK PROBLEM_____*****" )
    print("\n")
    # creating options
    while True:
        print("\n OPTIONS :- ")
        print("1.EXIT")        
        print("2.ADD NEW CONTACT")
        choice = input("Enter your choice in numbers : ")
        if choice == '1':
            print("Exiting the program")
            break
        elif choice == '2':
            print("\n Add your details :")
            address_book_system.create_contact()
        else:
            print("\n INVALID CHOICE, TRY AGAIN ")
        
    
if __name__ =="__main__":
    main()