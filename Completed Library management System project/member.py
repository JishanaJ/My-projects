# imports
from library import Librarian as libr

# Patron class

class Patron:
    """ this is the Patron class """
    def __init__(self, name, email, patron_id):
        """ this are the patron class attributes """
        self.name = name
        self.email = email
        self. patron_id = patron_id

    def search(self):
        """ this will enable the patron search a book """
        print("What do you want to do?: ")
        self.patron_search = input(" press 's' to search for a book:  \n press 'n' to see how many book are there: ")
        self.patron_search = self.patron_search.lower()
        if self.patron_search == "s":
            self.librarian_location = input("Enter Librarian location: ")
            try:
                self.librarian_id = int(input("Enter librarian id: "))
            except ValueError:
                print("Error! PLease enter a numerical input.")
            else:
                self.patron_book = input("Enter the title of the book you want to search: ")
                self.patron_book_result = libr(self.librarian_location, self.librarian_id)
                self.patron_book_result.search_book(self.patron_book)
                self.patron_book_result

        elif self.patron_search == "n":
            # see how many books are there
            self.librarian_location = input("Enter librarian location: ")
            try:
                self.librarian_id = int(input("Enter librarian ID: "))
            except ValueError:
                print("Error! enter a numerical input")
            else:
                self.available_books = libr(self.librarian_location, self.librarian_id)
                print("This are the available books. total is ({})".format(len(self.available_books.availabale_books)))
                for available_book in self.available_books.availabale_books:
                    print(f"-> {available_book}")
        else:
            print("Please enter either 's' or 'n'")
        
    def request(self):
        """ this enables the patron to see book requests """
        self.librarian_location = input("Enter Librarian location: ")
        self.librarian_id = input("Enter librarian id: ")
        self.book_request = input("Enter the book you want to request: ")
        self.librarian_instance = libr(self.librarian_location, self.librarian_id)
        self.librarian_instance.requested_book.append(self.book_request)
        print(f"Your request for  {self.book_request} has been sent.")
    

    def pay_fine(self):
        """ this will make the patron be able to pay fines """
        self.librarian_location = input("Enter Librarian location: ")
        self.librarian_id = input("Enter librarian id: ")
        self.pay_owned_fine = libr(self.librarian_location, self.librarian_id)
        
        self.payment_answer = input(f" Are you sure you want to pay {self.pay_owned_fine.total_payments} ? 'y' | 'n' ")
        self.payment_answer = self.payment_answer.lower()
        
        if self.payment_answer == "y":
            self.payment_amount = int(input("Enter the amount you want to pay: "))
            if self.payment_amount <= self.pay_owned_fine.total_payments:
                self.balance = self.pay_owned_fine.total_payments - self.payment_amount
                print("Thank you for paying! Your balance is: {}".format(self.balance))
            if self.payment_amount > self.pay_owned_fine.total_payments:
                print(f"The amount you are paying can not be above: {self.pay_owned_fine.total_payments}") 
        else:
            print("Please pay your fines ")

    def payment_details(self):
        """ this shows the payment details where the funds will go """
        self.bank_name = input("Enter bank name: ")
        self.account_number = int(input("Enter account number: "))
        self.branch_location = input("Enter branch location: ")

        print("Payment will be made to")
        print(f"Account number:\t {self.account_number}")
        print(f"Bank name:\t {self.bank_name}")
        print(f"Bank branch:\t {self.branch_location}")
 
# Patron_record child class 
class Patron_record(Patron):
    """ this is a child class of the parent Patron """
    def __init__(self, name, email, patron_id):
        super().__init__(name, email, patron_id)
        """ this are the attributes of the child class Pareon_record """
        self.patron_id = patron_id
        self.name  = name
        self.email = email
        self.book_type = ""
        self.date_of_membership = ""
        self.number_of_books_issued = 12
        self.maximum_number_limit = 100
        # To-do This should be entered by the necessary person
        self.phone_number = ["12345", "23456","34567"]
        self.phone_number_length = len(self.phone_number[0])
        self.fines_owed = ""

   