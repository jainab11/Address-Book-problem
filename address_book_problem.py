# this calss is for taking input from user for address book
class AddressBook:
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
        
def main():
    print("____________WELCOME TO ADDRESS BOOK PROBLE____________________")
    print("______________________________________________________________")
    obj_address_book = AddressBook() 
    obj_address_book.display()   
    
if __name__ == "__main__":
    main()