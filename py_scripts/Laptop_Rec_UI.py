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
user_name= ""	#placeholder for the name of the user
user_type = None #default case; determines if user is new, average, or experienced
user_input = ""	#placeholder for any input strings from the user
user_app = 2 #default case; determines what the user would be using the laptop for

budget = None #default case, $300
prompt_fin = 0 #default case, 0=continue prompting, 1=finish prompting
confidence = None #default case, determines how confident a person is with tech jargon.
dim_screen= None #default case, determines dimensions of screen.
memory= None #default case, determines how much memory a laptop must have.

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
	user_id+=1
	print("It's a pleasure to meet you, " +user_name+ ", we hope we can help you find the kind of laptop you want.")
	print(user_id)

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
	print("It's alright, knowing nothing is a start for knowing something, and that's why we're here to help you out and keep things simple as possible.")

def test_user_average():
	global user_type
	user_type=1
	print("Sweet, we'll try to keep things simple for you.")

def test_user_experienced():
	global user_type
	user_type=2
	print("Awesome, we'll take into account more precise details to fine tune the perfect laptop for you as we do this.")

def test_user_hopeless():
	global user_type
	user_type=0
	print("Don't worry, we're here to help people like yourself get started on the right foot.")

def test_user_narcissistic():
	global user_type
	user_type=2
	print("We admire your confidence. We aim to please you then.")

# The type of user
# Ask if they are tech savvy or not on a scale of 0-10.
# 0-3=NEW, 4-6=AVERAGE, 7-10=EXPERIENCED
# Lays initial pathway into new_user(), average_user(), and experienced_user()
def type_user():
	global user_name
	global user_type
	global confidence
	
	while(user_type==-1):
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
				budget=int(input("What is the maximum amount of money you are willing to spend on a laptop?\nAccepted price range is from $350 to $6500.\n(NOTE: Most laptops generally cost around $3425)\n>>>").replace(',',''))
			except:
				print("We're sorry, but we don't understand what you mean, " +user_name+". Please type a number.")
		if (budget<350) or (budget>6500):
			print("We don't have any products that will fit your budget.")
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
				budget=int(input("What is the maximum amount of money you are willing to spend on a laptop?\nAccepted price range is from $150 to $2500.\n(NOTE: Most laptops generally cost around $1325)\n>>>").replace(',',''))
			except:
				print("We're sorry, but we don't understand what you mean, " +user_name+". Please type a number.")
		if (budget<150) or (budget>2500):
			print("We don't have any products that will fit your budget.")
			budget=None
		else:
			return True

#Budget range
#Determine how much money the user is willing to spend.
def budget_amount():
	flag = False	#Used for breaking out of while loop
	print("The next thing we need to know now is your budget.")
	while (flag==False):
		#Gamer user
		if (gamer_user_budget()==True):
			flag=True
		#Study user
		if (study_user_budget()==True):
			flag=True
		


#Application
#What will the user be using the laptop for?
def application():
	global user_name
	print("Alright, "+user_name+", the most important part that we can ask you now is this: what do you intend on using this laptop for?")
	print("Here is a selection of options for you to pick from: gaming, ")

#Print statements for displaying screen size options
#Used for screen_size(); see below
def screen_size_print_options():
	print("The next thing we need to consider is how big you want your screen to be.\n")
	print("You have three options to choose from:")
	print("Option 1: 11.6\" to 13.5\". This is considered small and is useful for on the move users who like something portable.")
	print("Option 2: 13.6\" to 15.4\". This is considered medium and is useful for general use, including watching movies, office/school work, and gaming")
	print("Option 3: 15.5\" to 17.3\". This is considered large and is practical for stationary users and/or people who have difficulty with vision. Ideal for intensive gaming, video editing, art, or any large projects.\n")

#Screen size
#How big does the user want their screen to be?
def screen_size():
	global user_name
	global user_input
	global dim_screen
	flag=False	#Used for breaking out of the while loop.

	screen_size_print_options()
	while(flag==False):
		while(dim_screen==None):
				try:
					dim_screen=int(input("Please pick and type one of the three options (1 for small, 2 for medium, 3 for large)\n>>>"))
				except:
					print("We're sorry, but we can't understand what you mean by that, " +user_name+". Please make sure you are typing a number.")
		if(dim_screen<1) or (dim_screen>3):
			print("We apologize, but that is not a valid input.")
			dim_screen=None
		else:
			flag=True

#Print statements for displaying storage size options
#Used for storage_size(); see below
def storage_size_print_options():
	print("The next thing to calculate is how much storage or memory space you want your laptop to have.\n")
	print("You have three options to choose from:")
	print("Option 1: 11.6\" to 13.5\". This is considered small and is useful for on the move users who like something portable.")
	print("Option 2: 13.6\" to 15.4\". This is considered medium and is useful for general use, including watching movies, office/school work, and gaming")
	print("Option 3: 15.5\" to 17.3\". This is considered large and is practical for stationary users and/or people who have difficulty with vision. Ideal for intensive gaming, video editing, art, or any large projects.\n")


#Storage capacity
#How much memory/space does the user want their laptop to have?
#def storage_size():


#Prompts dedicated to new, inexperienced users.
#Must be broken down into:
#Budget
#Application (what are they using the laptop for)
#Screen size (will they be moving a lot or staying in one spot)
#Storage (would they like a lot of storage space)


###MAIN FUNCTION###
#greeting()
#type_user()
#budget_amount()
#screen_size()
