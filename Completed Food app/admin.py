import time
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

class admin:
    def __init__(self):
        pass


    def admin_functions(self):
        print(" 1. View  the food item and related info\n 2. Add more food items\n 3. Edit information of food items")
        print("what do you want to do?")
        y=int(input())
        if y==1:
            self.show_food_list()
        elif y==2:
            self.add_more_food()
        elif y==3:
            self.edit_food_info()
        print("Do you want to be here more?Enter yes or no :  ")
        x=input()
        if x=="yes":
            self.admin_functions()
        else:
            return


    def login_admin(self):
        print("enter your email id")
        x=input()
        if x=="admin@gmail.com":
            print("enter password")
            if input()=="admin":
                print('Logging in...')
                time.sleep(1)
                self.admin_functions()
	        
    
    def show_food_list(self):
            print (" Here is the Menu")
            print(food_info)
    def add_more_food(self):
                   a={}
                   food_info[input("enter food id")]=a
                   a["Name"]=input("enter name of food item")
                   a["Quantity"]=input("enter quantity per serving")
                   a["price"]=int(input("enter price per serve"))
                   a["discount"]=int(input("offer customer some discount"))
                   a["stocK_left"]=int(input("enter stocks left"))
               
               
    def edit_food_info(self):
        print("enter id of food item you want to make changes on ")
        x=input()
        if x not in food_info:
            print("There is no food item with this id")
        else:
            print(food_info[x])
            print("1. change the name \n 2. change the quantity \n 3. change the price \n 4. change discount \n 5. change the stock left \n 6. delete the fod item from the menu")
            y=int(input())
            if y==1:
                food_info[x]["Name"]=input("enter new name")
            elif y==2:
                food_info[x]["Quantity"]=input("enter new quantity")
            elif y==3:
                food_info[x]["Pice"]=int(input("enter new price"))
            elif y==4:
                food_info[x]["Discount"]=int(input("enter new discount"))
            elif y==5:
                food_info[x]["stock left"]=int(input("enter new stock left"))
            elif y==6:
                del food_info[x]
            else:
                print("Data has been updated")
                return
        print("Data Updated")