'''
Overview: User-input interface for laptops they should be recommended.

Details:
-User is given an initial prompt (a greeting + a brief introduction)
-User wants a laptop that bests suits their needs.
-Each prompt would slowly break down various questions regarding different computer specifications (e.g. memory, screen size).
-There would be no more than 5-10 questions.
-Program offers a list of suggestions from database based on user specs.

Implementation Details:
-Create functions for different categories of laptop specs
-Establish global variables that could act as flags based on user input
-Use nested conditional statements under an if-else statement that divides the program between new and experienced computer users (i.e. if? new#1: else? exp#2).
-Keep track of how many people used this program via a counter system in the greeting code.
'''
###LIBRARIES###
'TO BE DECIDED'

###GLOBAL VARIABLES###

user_id = 0 #default case
user_name = ""	#placeholder for the name of the user
user_type = None #default case; determines if user is new, average, or experienced
user_input = ""	#placeholder for any input strings from the user
user_app = None #default case; determines what the user would be using the laptop for

budget = None #default case, $300
prompt_fin = 0 #default case, 0=continue prompting, 1=finish prompting
confidence = None #default case, determines how confident a person is with tech jargon.
dim_screen = None #default case, determines dimensions of screen.
laptop_purpose = None #default case, original answer of what the user would be using the laptop for in user_app; utilized in closing()
RAM = None #default case, determines how much RAM a laptop must have.
storage_cap = None #default case, determines how much storage a laptop must have.

#Placeholder statements used in closing functions.
laptop_purpose_print = ""
budget_print = ""
screen_size_print_closing = ""
storage_size_print_closing = ""
RAM_capacity_print_closing = ""

rating = 0 #default case, will be divided into 3 groups: none → 2, 3 → 5)

###FUNCTIONS###

# Greeting
# Say hello to the user
# Ask for their name
# Introduce the user to the program
# Increment the user_id by 1 (PROTOTYPE)
def greeting():
	global user_id
	global user_name
	
	print("Hello there! This is a laptop-recommendation service designed to personally help you find the right laptop that fits your needs.")
	user_name=input("Before we dive into the details, what's your name?\n>>>")
	#user_id+=1
	print("It's a pleasure to meet you, " +user_name+ ", we hope we can help you find the kind of laptop you want.\n")
	#print(user_id)


#Prompt user for how confident/familiar they are with laptops and their specs.
# Is confidence level correctly inputted as an integer?
# Used for type_user(); see below
def confidence_lvl_int():
	global confidence
	while(confidence==None):
		try:
			confidence=int(input("On a scale of 0 to 10, how familiar are you with laptops and their specs in general?\n>>>"))
		except:
			print("We're sorry, but we don't understand what you mean, " +user_name+". Please type a number.")

#5 prompts based on level of experience for users.
#Used for type_user(); see below
def test_user_newbie():
	global user_type
	user_type=0
	print("\nIt's alright, knowing nothing is a start for knowing something, and that's why we're here to help you out and keep things simple as possible.\n")
	return user_type

def test_user_average():
	global user_type
	user_type=1
	print("\nSweet, we'll try to keep things simple for you.\n")
	return user_type

def test_user_experienced():
	global user_type
	user_type=2
	print("\nAwesome, we'll take into account more precise details to fine tune the perfect laptop for you as we do this.\n")
	return user_type

def test_user_hopeless():
	global user_type
	user_type=0
	print("\nDon't worry, we're here to help people like yourself get started on the right foot.\n")
	return user_type

def test_user_narcissistic():
	global user_type
	user_type=2
	print("\nWe admire your confidence. We aim to please you then.\n")
	return user_type

# The type of user
# Ask if they are tech savvy or not on a scale of 0-10.
# 0-3=NEW, 4-6=AVERAGE, 7-10=EXPERIENCED
# Lays initial pathway into new_user(), average_user(), and experienced_user()
def type_user():
	global user_name
	global user_type
	global confidence
	
	while(user_type==None):
		#Ask for input; Is the input an integer?
		confidence_lvl_int()
			
		#For the newbies.
		if (confidence<=3) and (confidence>=0):
			test_user_newbie()
		#For the average.
		elif (confidence>=4) and (confidence<=6):
			test_user_average()
		#For the experienced.
		elif (confidence>=7) and (confidence<=10):
			test_user_experienced()
		#For the real smartasses.
		elif (confidence>=11):
			test_user_narcissistic()
		#For anyone who is just somehow negative.
		elif (confidence<0):
			test_user_hopeless()
		else:
			print("We're sorry, but we don't understand what you mean, " +user_name+". Please type a number.")
	return user_type

#Print statements for application type options
#Used for application(); see below	
def application_print_options():
	global user_name
	print("Alright, "+user_name+", the most important question that we can ask you now is this: what do you intend on using this laptop for?")
	print("Here is a selection of five options for you to pick from:") 
	print("Option 1: Gaming")
	print("Option 2: Office/School work")
	print("Option 3: Advanced Projects (including video-editing, drawing, program development, etc.)")
	print("Option 4: Light usage/general documentation (family/friends photos and videos, filing taxes, reading E-books, etc.).")
	print("Option 5: Other/Unspecified (We would choose from a general standard of laptops if none of the above options fit your criteria)\n")

#Application
#What will the user be using the laptop for?
def application():
	global user_name
	global user_app
	global laptop_purpose
	flag=False
	
	application_print_options()
	while(flag==False):
		while(user_app==None):
				try:
					user_app=int(input("Please pick and type one of the five options (1, 2, 3, 4, or 5).\n>>>"))
				except:
					print("We're sorry, but we can't understand what you mean by that, " +user_name+". Please make sure you are typing a number.")
		#Laptop_purpose will be used later for the closing().
		laptop_purpose=user_app
		if(user_app<1) or (user_app>5):
			print("We apologize, but that is not a valid input.")
			user_app=None
		else:
			#Make user_app set to gamer regardless if they are option 3 (most specs for gamers would apply to advanced projects)
			if (user_app==1) or (user_app==3):
				user_app=1
			#Make user_app set to office/school work even if they are options 4 or 5 (office/school work dedicated laptops can apply to all 3 options)
			if (user_app==2) or (user_app==4) or (user_app==5):
				user_app=2
			flag=True

#Two different prompts based on what the user would be using the laptop for.
#Reminder: user_app==1 means gaming; 2 means study.
#Used for budget_range(); see below
def gamer_user_budget():
	global budget
	global user_name
	global user_app
	if (user_app==1):
		while(budget==None):
			try:
				budget=int(input("What is the maximum amount of money you are willing to spend on a laptop?\nAccepted price range is from $350 to $6500.\n(NOTE: Most laptops generally cost around $3425)\n>>>").replace(',','').replace('$',''))
			except:
				print("We're sorry, but we don't understand what you mean, " +user_name+". Please type a number.")
		if (budget<350) or (budget>6500):
			print("We don't have any products that will fit that budget.")
			budget=None
		else:
			return True

def study_user_budget():
	global budget
	global user_name
	global user_app
	if (user_app==2):
		while(budget==None):
			try:
				budget=int(input("What is the maximum amount of money you are willing to spend on a laptop?\nAccepted price range is from $150 to $2500.\n(NOTE: Most laptops generally cost around $1325)\n>>>").replace(',','').replace('$',''))
			except:
				print("We're sorry, but we don't understand what you mean, " +user_name+". Please type a number.")
		if (budget<150) or (budget>2500):
			print("We don't have any products that will fit that budget.")
			budget=None
		else:
			return True

#Budget range
#Determine how much money the user is willing to spend.
def budget_amount():
	global budget
	flag = False	#Used for breaking out of while loop
	print("\nAwesome! The next thing we need to know now is your budget.")
	while (flag==False):
		#Gamer user
		if (gamer_user_budget()==True):
			flag=True
		#Study user
		if (study_user_budget()==True):
			flag=True
	return budget

#Print statements for displaying screen size options
#Used for screen_size(); see below
def screen_size_print_options():
	print("\nAlright, now the next thing we need to consider is how big you want your screen to be.\n")
	print("You have three options to choose from:")
	print("Option 1: 11.6\" to 13.5\". This is considered small and is useful for on the move users who like something portable.")
	print("Option 2: 13.6\" to 15.4\". This is considered medium and is useful for general use, including watching movies, office/school work, and gaming")
	print("Option 3: 15.5\" to 17.3\". This is considered large and is practical for stationary users and/or people who have difficulty with vision. Ideal for intensive gaming, video editing, art, or any projects.")
	print("Option 4: 17.3\" to 18.4\". This is considered very large and is practically a portable desktop. However, its extra large size makes it difficult to transport, though it is useful for intensive gaming, large-scale projects that require a lot of visuals, or a cinematic movie watching experience.\n")

#Screen size
#How big does the user want their screen to be?
def screen_size():
	global user_name
	global dim_screen
	flag=False	#Used for breaking out of the while loop.

	screen_size_print_options()
	while(flag==False):
		while(dim_screen==None):
				try:
					dim_screen=int(input("Please pick and type one of the four options (1 for small, 2 for medium, 3 for large, 4 for very large)\n>>>"))
				except:
					print("We're sorry, but we can't understand what you mean by that, " +user_name+". Please make sure you are typing a number.")
		if(dim_screen<1) or (dim_screen>4):
			print("We apologize, but that is not a valid input.")
			dim_screen=None
		else:
			flag=True
	return dim_screen

#Print statements for displaying storage size options
#Used for storage_size(); see below
def storage_size_print_options():
	print("\n Good, then the next thing to calculate is how much storage space you want your laptop to have.\n")
	print("You have three options to choose from:")
	print("Option 1: 64GB to 256GB. This is considered small and is useful for storing notes, pictures, short videos, and a few low-intensive games. This is generally meant for people who do not plan on storing a lot of information on their device. Good for use in the span of less than five years.")
	print("Option 2: 256GB to 512GB. This is considered medium and is useful for general use, including watching movies, office/school work involving a lot of documents and files, and gaming. Good for use in the span of five to ten years.")
	print("Option 3: 512GB and above. This is considered large and is ideal for intensive gaming, video editing, art, or any large-scale projects. Please note that this means that laptops with this much storage space are much more expensive. Good for use for over ten years generally.\n")
	print("Computer Terms: MB= megabyte, GB= gigabyte, TB= terabyte\nMB < GB < TB\nThere are 1000MB in 1GB; 1000GB in 1TB\n")


#Storage capacity
#How much space does the user want their laptop to have?
def storage_size():
	global user_name
	global storage_cap
	flag=False	#Used for breaking out of the while loop.

	storage_size_print_options()
	while(flag==False):
		while(storage_cap==None):
				try:
					storage_cap=int(input("Please pick and type one of the three options (1 for small, 2 for medium, 3 for large)\n>>>"))
				except:
					print("We're sorry, but we can't understand what you mean by that, " +user_name+". Please make sure you are typing a number.")
		if(storage_cap<1) or (storage_cap>3):
			print("We apologize, but that is not a valid input.")
			storage_cap=None
		else:
			flag=True
	return storage_cap
#Print statements for displaying RAM options
#Used for RAM_capacity(); see below
def RAM_print_options():
	print("\nNow the next thing to do is to understand and choose how much RAM you want your laptop to have.\n")
	print("RAM stands for Random-Access Memory. People sometimes confuse RAM with storage space because both of them use GB as a unit of measurement.")
	print("RAM determines how many programs you can be running at the same time. Think of it like a desk: if you have a lot of desk space (i.e. a large amount of RAM), you have a lot more space to spread out your papers and read them all at once.\nOn the other hand, if you have a small amount of desk space (i.e. a small amount of RAM), you have less space to look at your papers and have to be selective about which ones to read at a time.\n IN OTHER WORDS: RAM determines how well you can multi-task on your laptop at one time.\n")
	print("You have three options to choose from:")
	print("Option 1: 4GB. This is a small amount of RAM that enables you to do a few tasks at a time. It is meant for low-intensity work and usage (you can still watch movies or use this for work, but you may experience slowdown.")
	print("Option 2: 8GB. This is a decent amount of RAM that allows for more tasks to be done at once. It gets a majority of jobs done and is reliable all-around. Still, not ideal for gaming purposes and is mostly meant for work.")
	print("Option 3: 16GB. This is a standard amount of RAM that lets you to do work on various tasks on a daily basis. It's a good all-rounder, perfectly capable for gaming, work, and is a recommended amount for most users.")
	print("Option 4: 32GB and above. This is an exceptional amount of RAM that is generally more expensive than its 16GB counterpart, but is greatly ideal for people specializing in a specific work field that demands a great deal of power and energy for use. Think of this like a workbench for a craftsman. It also makes for a fantastic gaming laptop.\n")

def RAM_capacity():
	global user_name
	global RAM
	flag=False	#Used for breaking out of the while loop.

	RAM_print_options()
	while(flag==False):
		while(RAM==None):
				try:
					RAM=int(input("Please pick and type one of the four options (1 for 4GB, 2 for 8GB, 3 for 16GB, 4 for 32GB and above)\n>>>"))
				except:
					print("We're sorry, but we can't understand what you mean by that, " +user_name+". Please make sure you are typing a number.")
		if(RAM<1) or (RAM>4):
			print("We apologize, but that is not a valid input.")
			RAM=None
		else:
			flag=True
	return RAM

#Prompts dedicated to new, inexperienced users.
#Must be broken down into:
#Budget
#Application (what are they using the laptop for)
#Screen size (will they be moving a lot or staying in one spot)
#Storage (would they like a lot of storage space)
#Ram (how powerful do they need their laptops to be)

def laptop_purpose_closing():
	global laptop_purpose
	global laptop_purpose_print
	if (laptop_purpose==1):
		laptop_purpose_print="1- Gaming"
	elif(laptop_purpose==2):
		laptop_purpose_print="2- Office/School work"
	elif(laptop_purpose==3):
		laptop_purpose_print="3- Advanced Projects"
	elif(laptop_purpose==4):
		laptop_purpose_print="4- Light Usage/General Documentation"
	else:
		laptop_purpose_print="5- Other/Unspecified"
	return (laptop_purpose_print)

def budget_closing():
	global budget_print
	global budget
	budget_print=str(budget)
	return (budget_print)
	
def screen_size_closing():
	global screen_size_print_closing
	if(dim_screen==1):
		screen_size_print_closing='1- 11.6\" to 13.5\"'
	elif(dim_screen==2):
		screen_size_print_closing='2- 13.6\" to 15.4\"'
	elif(dim_screen==3):
		screen_size_print_closing='3- 15.5\" to 17.3\"'
	else:
		screen_size_print_closing='4- 17.4\" to 18.4\"'
	return (screen_size_print_closing)
	
def storage_size_closing():
	global storage_size_print_closing
	if(storage_cap==1):
		storage_size_print_closing="1- 64GB to 256GB"
	elif(storage_cap==2):
		storage_size_print_closing="2- 256GB to 512GB"
	else:
		storage_size_print_closing="3- 512GB and above"
	return (storage_size_print_closing)

def RAM_capacity_closing():
	global RAM_capacity_print_closing
	if(RAM==1):
		RAM_capacity_print_closing="1- 4GB"
	elif(RAM==2):
		RAM_capacity_print_closing="2- 8GB"
	elif(RAM==3):
		RAM_capacity_print_closing="3- 16GB"
	else:
		RAM_capacity_print_closing="4- 32GB"
	return (RAM_capacity_print_closing)

def closing():
	global user_name
	flag=False
	recheck_flag=False
	
	print("\nThank you so much for your answers, " + user_name + "! Here is a record of your inputs, and we want to make sure we got your answers right. Please look over your answers and tell us if you want to change anything before we offer our recommendations.\n")
	
	print("(1)Laptop Purpose: " + laptop_purpose_closing())
	print("(2)Budget: $" + budget_closing())
	print("(3)Screen Size: " + screen_size_closing())
	print("(4)Storage Size: " + storage_size_closing())
	print("(5)RAM Capacity: " + RAM_capacity_closing())
	'''
	print (user_name)
	print (confidence)
	print (user_type)
	print (user_app)
	print (budget)
	print (dim_screen)
	print (storage_cap)
	print (RAM)
	'''
	while (flag==False):
		end_prompt=input("\nDid we get it right? (Y\\N)\n>>>")
		if (end_prompt=="Y") or (end_prompt=="y"):
			print("Awesome.")
			flag=True
		elif (end_prompt=="N") or (end_prompt=="n"):
			print("Shoot, we're extremely sorry. Please reload the program to re-input answers")
			flag=True
		else:
			print("Sorry, we didn't quite catch that. Please type 'Y' or 'N'.")

###MAIN FUNCTION###

def main():
	global b, ss, sc, r
	greeting()
	type_user()
	#if the user is experienced at laptops
	if (type_user()==2):
		print("EXPERIENCED USER")
		application()
		b = budget_amount() # return budget
		ss = screen_size() # returns dim_screen
		sc = storage_size() # returns storage_cap
		r = RAM_capacity() # returns RAM
		closing()
	#if the user is average at laptops
	elif (type_user()==1):
		print("AVERAGE USER")
		application()
		b = budget_amount()
		ss = screen_size()
		sc = storage_size()
		r = RAM_capacity()
		closing()
	#if the user is new at laptops
	else:
		print("NEW USER")
		application()
		b = budget_amount()
		ss = screen_size()
		sc = storage_size()
		r = RAM_capacity()
		closing()

main()
