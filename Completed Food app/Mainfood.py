import admin
import user
if __name__ == '__main__':
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
    main_input = 1
    while True:
        print(" Hello.. \n Welcome to Jishu's Food")
        print("1. Admin \n2. customer ")
        main_input=int(input("Select who you are (choose a number): "))
        if main_input == 1:
            admin1 = admin.admin()
            admin1.login_admin()
        elif main_input ==2:
            user1 = user.user()
            user1.login_user()
        else:
            print(" Invalid input ")
            continue