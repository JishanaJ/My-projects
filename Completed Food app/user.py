list_of_names=[]
list_of_DOB=[]
list_of_contact_num=[]
list_of_email=[]
list_of_password=[]
users_list=[list_of_names,list_of_DOB,list_of_contact_num,list_of_email,list_of_password]

list_of_food=[ "tandoori chicken (4 pieces) [INR 240]","vegan burger (1piece)[INR 320]","traffle cake (500gm)[INR 900]"]

food_info={"10001":{"Name":"tandoori chicken","Quantity": " 4 pieces","Price":240,"Discount":0,"stock left":10},
                "10002":{"Name":"vegan burger","Quantity":"1 piece","Price":320,"Discount":0,"stock left":10},
                 "10003":{"Name":"traffle cake","Quantity":"500 gram","Price":900,"Discount":0,"stock left":10}}

class user:
    def __init__(self):
        pass

    def  register(self):
        name=self.NAME()
        dob=self.DOB()
        contact=self.contact_num()
        email_id=self.email()
        Password=self.password()
    
   
    def NAME(self):
        print("enter name")
        name=input()
        self.name=name
        list_of_names.append(name)


    def DOB(self):
        print("enter your date of birth in format dd-mm-yyyy")
        DOB=input().split("-")
        self.dob=DOB
        list_of_DOB.append(DOB)


    def contact_num(self):
        print("enter 10 digit contact number")
        num=input()
        import re
        if (re.search("[0-9]{10}",num)):
            self.contact=num
            list_of_contact_num.append(num)
            return
        else:
            print("contact number is 10 digits number ,fill it again")
            self.contact_num()


    def email(self):
        print("enter email address $$note: email_address must start with an alphabet ,then it shoulh have one or more digit and  should have a domain @gmail.com $$")
        email_add=input()
        import re
        if email_add in list_of_email:
            print("this email id is already registered ,please login")
            list_of_names.pop(len(list_of_names)-1)
            list_of_DOB.pop(len(list_of_DOB)-1)
            list_of_contact_num.pop(len(list_of_contact_num)-1)
        else:
            if( re.search("^[a-zA-Z]+[0-9]+.*@gmail.com$",email_add)):
                list_of_email.append(email_add)
                self.email=email_add
                #self.password()
            else:
                print("email_address must start with an alphabet ,then it shoulh have one or more digit and  should have a domain @gmail.com")
                self.email()


    def password(self):
        print("enter your password $$note: password must begin with an alphabet ,must contain one or more digit and a special character$$")
        word=input()
        import re
        if(re.search("[a-zA-Z]+[0-9]+.",word)):
            self.password=word
            list_of_password.append(word)
        else:
            print("password must begin with an alphabet ,must contain one or more digit and a special character")
            self.password()
        print("registered successfully done")
        self.login_user()

    def show_food_list(self):
                   print(food_info)
           
    def order(self):
        self.list_of_order=[]
        for i in range(len(list_of_food)):
            print("enter",i+1,"for",list_of_food[i])
        z=list(map(int,input().split(" ")))
        for i in z:
            print("You have selected ",list_of_food[i-1])
        print("Do you want to place your order? enter OK to place your order")
        if(input()=="OK"):
            for i in z:
                self.list_of_order.append(list_of_food[i-1])
            print("Your order has been placed,Enjoy your meal")
        else:
            return


    def login_user(self):
        print("enter your email address")
        x=input()
        if x in list_of_email:
            print("enter password")
            y=input()
            if y==list_of_password[list_of_email.index(x)]:
                print("(What do you want to do?")
                print("\n 1.register\n 2. Place an order \n 3.Check order history \n 4. Update profile 5. Veiw menu" )
                z=int(input())
                if z==1:
                    self.register()
                elif z==2:
                    print(list_of_food)
                    if input("want to order something,press yes or no")=="yes":
                        self.order()
                    else:
                        pass
                elif z==3:
                    self.show_order()
                elif z==4:
                    self.update_profile()
                elif z==5:
                    self.show_food_list()
            else:
                print("password does not match with the email id")
        else:
            print("the email id is not registered let's go with registration first !!!! ")
            self.register()


    def show_order(self):
        print(self.list_of_order)


    def update_profile(self):
        print("NAME",self.name)
        print("DOB",self.dob)
        print("contact",self.contact)
        print("Email id",self.email)
        print("Password",self.password)
        x=input("what do you want to update")
        if(x=="NAME"):
            name= self.NAME()
            print("profile updated")
        elif(x=="DOB"):
            dob= self.DOB()
            print("profile updated")
        elif(x=="contact number"):
            contact=self.contact_num()
            print("profile updated")
        elif(x=="email Id"):
            email= self.email()
            print("profile updated")
        elif(x=="password"):
            Password=self.password()
            print("profile updated")
        else:
            print('You have not selected anythng to be updated')