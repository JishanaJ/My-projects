# import relevant files
import sys 
import time
import book as vnd 
import library as lbr 
from member import Patron as ptr
from member import Patron_record as ptrr
while (True):
    # The menu
    print("MENU")
    print(" 1. Librarian \n 2. Member")
    try:
        choice = int(input("Select who you are (choose a number): "))
    except ValueError:
        print("you have not entered a numerical input! \nplease enter a number")
        
    # Librarian choice 

    if choice == 1:
        print('Hello!')
        time.sleep(1)
        print('please login to continue')
        time.sleep(2)
        
        user_id = input("please enter your email id:  ")
        time.sleep(1)
        password = input("please enter your password:  ")
        time.sleep(1)
        
        print('Logging in...')
        time.sleep(1)
        print('Please select any item from the menu:')
        print(" 1. Check issued books \n 2. Search for a book \n 3. Verify a member \n 4. Issue a book \n 5. Check payments ")
        while (True):
            # Handling Value Error
            try:
                librarian_choice_one = int(input("What would you like to do? :"))
            except ValueError:
                print("you have not entered a numerical input! \nplease enter a number")
                break
            else:
                librarian_location = input("Enter your location: ")
                # handling ValueError
                try:
                    librarian_id = int(input("Enter your librarian ID: "))
                except ValueError:
                    print("Error! Please enter a numerical input")
                else: 
                    logged_in_user = lbr.Librarian(librarian_location, librarian_id)
            
                    if librarian_choice_one == 1:
                        logged_in_user.issue_status()

                    elif librarian_choice_one == 2:
                        check_book = input("Enter the book you want to check: ")
                        logged_in_user.search_book(check_book)

                    elif librarian_choice_one == 3:
                        verify_member = input ("Enter a member to verify: ")
                        logged_in_user.verify_member(verify_member)

                    elif librarian_choice_one == 4:
                        issue_book = input("Enter the book you want to issue: ")
                        logged_in_user.issue_book(issue_book)
                    elif librarian_choice_one == 5:
                        logged_in_user.payment()

    # Patron Choice            
    elif choice == 2:
        print('Hello!')
        time.sleep(1)
        print('please login to continue')
        time.sleep(2)
        
        user_id = input("please enter your email id:  ")
        time.sleep(1)
        password = input("please enter your password:  ")
        time.sleep(1)
        
        print('Logging in...')
        time.sleep(1)
        print('Please select any item from the menu:')
        print(" 1. search a book \n 2. Request a book \n 3. Pay fine \n 4. Payment details ")
        # Handling ValueError
        try:
            patron_choice  = int(input("Enter what you want to do: "))
        except ValueError:
            print("you have not entered a numerical input! \nplease enter a number")
        else:
            patron_name = input("Enter Member name: ")
            patron_email = input("Enter Member email: ")

            # handling ValueError
            try:
                patron_id = int(input("Enter Member Id: "))
            except ValueError:
                print("you have not entered a numerical input! \nplease enter a number")
            else:
                logged_in_patron = ptr(patron_name, patron_email, patron_id)

                if patron_choice == 1:
                    logged_in_patron.search()
                elif patron_choice == 2:
                    logged_in_patron.request()
                elif patron_choice == 3:
                    logged_in_patron.pay_fine()
                elif patron_choice == 4:
                    logged_in_patron.payment_details()
                else:
                    print("You have entered an invalid choice!")

 



