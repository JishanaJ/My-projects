#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#-super user
#- - sign up 
# - login
#- - - Quiz
#- - - - Create quiz
#- - - - - Difficulty level
# - - - - Topic
#- - - - Read quiz
#- - - - Add User
#- - - - Update quiz
#- - - - Delete quiz
#-user
#- - login
#- - - Take Quiz
#- - - view topics

## final score and right ans
## user details and result after quiz


import time

class question:
	options=[]
	answers=[]
	levels=[]
	topics=[]
	prompt=[]
	
	def __init__(self):
		pass
		
	def addquestion(self):
		T=input("Topic:")
		L=input("Level:")
		S=input("Enter the question:")
		question.prompt.append(S)
		question.topics.append(T)
		question.levels.append(L)
		
		l1=[]
		for i in range(4):
			l1.append(input("Enter the option number"+str((i+1))+":"))
		question.options.append(l1)
		
		ans=input("Which is the currect option? 1/2/3/4:")
		question.answers.append(int(ans))
        
		print("New Question successfully added.")
		inp=input("Press 1>> Add another Question \n Press 2>>return to main menu\n\n")
		if inp=='1':
			self.addquestion()
		if inp=='2':
			self.admin_mainmenu()
            
	def displayallquestion(self):
		print("Total number of questions are:", len(self.prompt))
		print("\n")
		for i in range(len(question.prompt)):
			print("question "+str(i+1)+" "+self.prompt[i])
			for j in range(len(question.options[i])):
				print(str(j+1)+")"+str(question.options[i][j]))
				print("\n")
		inp=input("Press 1>> return to main menu \n Press 2>>Logout\n\n")
		if inp=='1':
			self.admin_mainmenu()
		if inp=='2':
			self.admin_logout()
            
	def deletetopic(self):
		print("Which topic you want to delete:")
		inpdelete=input("Topic:")
		if inpdelete in question.topics:
			question.topics.remove(inpdelete)
			print("Topic removed successfully")
		else:
			print("Topic is not present in the list")
			print("\n\n")
		inp=input("Press 1>> return to main menu \n Press 2>>Logout\n\n")
		if inp=='1':
			self.admin_mainmenu()
		if inp=='2':
			self.admin_logout()
       
	def Updatetopic(self):
		print("You can remove a topic and add a new topic here")
		print("Which topic you want to remove:")
		inpdelete=input("Topic:")
		if inpdelete in question.topics:
			question.topics.remove(inpdelete)
			print("Topic removed successfully")
		else:
			print("Topic is not present in the list")
			print("\n\n")
		print("Which is the topic you want to add:")
		T=input("Topic:")
		question.topics.append(T)
		print("Topic successfully Updated.")
		print("\n\n")
		inp=input("Press 1>> return to main menu \n Press 2>>Logout\n\n")
		if inp=='1':
			self.admin_mainmenu()
		if inp=='2':
			self.admin_logout()
        
        
	def viewtopics(self):
		a=set(question.topics)
		print(a)
		inp=input("Press 1>> return to main menu \n Press 2>>Logout\n\n")
		if inp=='1':
			self.main_menu()
		if inp=='2':
			self.member_logout()
        
	@classmethod
	def run_test(cls):
		score=0
		for S in range(len(cls.prompt)):
			print("Topic: "+cls.topics[S])
			print(cls.prompt[S])
            
			for i in range(len(cls.options[S])):
				print(str(i+1)+")"+str(cls.options[S][i]))
			print("Question level: ",cls.levels[S])
			answer=int(input("Enter option number as answer: "))
			print("\n")
            
			if answer==cls.answers[S]:
				score+=1
			print("\n")
			print("You got ",str(score),"/",str(len(cls.prompt)),"correct.")
		print("Thank you for taking the Quiz.. keep learning..!!")
		print("User Details:",User.list_of_Users.values()) 
		print("Currect answers are:",question.answers)
		inp=input("Press 1>> return to main menu \n Press 2>>Logout\n\n")
		if inp=='1':
			cls.main_menu()
		if inp=='2':
			cls.member_logout()
            
            
class User(question):
	list_of_Users = {}
	member_login_details={}
    
					
	def admin_home(self):
		self.start_action = input("Press 1 -- Superuser \nPress 2 -- Member\n")
		if self.start_action == '1':
            
			self.ad_action = input('Press 1 to Sign Up \nPress 2 to Log in\n')
            
			if self.ad_action == '1':
				self.new_admin()
                
			elif self.ad_action == '2':
				self.login_admin()
                
			else:
				print('Invalid Input')
				self.admin_home()
                
		elif self.start_action == '2':
			self.member_login()
                
		else:
			print('Invalid Input')
			self.admin_home()

            
	def member_login(self):
        
		print('User LOG IN!')
        
		self.phn_no= input("Enter Phone Number:")
		self.password= input("Enter Password:")
		if self.phn_no in User.list_of_Users:
			if self.password in User.member_login_details[self.phn_no]:
				print("User Logged in Successfully")
				self.member_log_in= True
				self.main_menu()
            
			else:
				print("Incorrect credentials")
				self.member_log_in= False
				self.member_login()
		else:
			print('User not signed up')
			self.admin_home()
            
	def main_menu(self):
		print('-------------------------------MAIN MENU------------------------------------')
		self.main_action = input("Press 1 >> Quiz Topics \nPress 2 >> take Quiz \nPress 0 >> Log Out\n")
		if self.main_action == "1":
			self.viewtopics()
		elif self.main_action == "2":
			self.__class__.run_test()
		elif self.main_action == '0':
			self.member_logout()
		else: 
			print(" Input does not match. Try again.")
			self.main_menu()

	def member_logout(self):
		self.member_log_in= False
		print("Member logged out.")
		print('Redirecting...')
		time.sleep(1)
		self.admin_home()
        
class admin(User):

	list_of_admins={}
	login_admin=[]
    
    
	def __init__ (self):
		print('Quiz Management')
		self.admin_home()
        
   
                
	def new_admin(self):
		print('<< Admin Sign Up >>')
        
		self.username = input("Enter Username:")
		self.password = input("Enter Password:")
        
		if self.username in admin.list_of_admins: 
			print("The username is already taken. Please try again with different combination.")
			self.new_admin()
            
		else:
			admin.list_of_admins[self.username]=[self.password]
			print("New admin successfully added")
			time.sleep(1)
			self.login_admin()

	def login_admin(self):
		print("<< Admin Log in >>")
		self.username = input("Enter Username:")
		self.password = input("Enter Password:")
		if self.username in admin.list_of_admins :
			if self.password in admin.list_of_admins[self.username]:
				print("Logged in successfully")
				self.admin_log_in= True
				self.admin_mainmenu()
			else:
				print("Incorrect credentials")
				self.admin_log_in= False
				self.login_admin()
                
		else:
			print('Admin not signed in')
			time.sleep(1)
			print('Redirecting to sign up page...')
			self.new_admin()
            
	def admin_mainmenu(self):
		print('---------------------------------------------------------------------------------------------------------------------')
		self.main_menu_action = input('Press 1 >> Add Question \nPress 2 >> View all questions \nPress 3 >> Delete topic\nPress 4 >> Add User \nPress 5 >> Update topic\nPress s 0 >> Logout\n')
		if self.main_menu_action == '1':
			self.addquestion()
		elif self.main_menu_action == '2':
			self.displayallquestion()            
		elif self.main_menu_action == '3':
			self.deletetopic()
		elif self.main_menu_action == '4':
			self.adduser()  
		elif self.main_menu_action == '5':
			self.Updatetopic()
		elif self.main_menu_action == '0':
			self.admin_logout()
             
		else:
			print('Invalid Input')
			self.admin_mainmenu()
            
	def adduser(self):

		print("All the details are mandatory to enter. Fill Carefully.")
		self.name = input("Enter Full Name:")
		self.phn_no = input("Enter Contact No:")
		self.password = input("Enter Password:")
		User.member_login_details[self.phn_no] = self.password
		User.list_of_Users[self.phn_no] = {"Name" : self.name, "Phone Number" : self.phn_no}
		print("New member successfully added.")

                                            
		self.temp_action = input("Press 1 >> Enter New Member \nPress 0 >> Main Menu\n")
		if self.temp_action == '1':
			self.add_member()
		elif self.temp_action == '0':
			self.admin_mainmenu()
		else:
			print('Invalid Input')
			print('Redirecting...')
			time.sleep(1)
			self.admin_mainmenu()
                       
	def admin_logout(self):
        
		self.admin_log_in= False
		print("Admin logged out.")
		print('Redirecting...')
		time.sleep(1)
		self.admin_home()                  
            
s= admin()     


# #### 

# In[ ]:




