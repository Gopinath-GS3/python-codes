myName = input("Enter your name: ")
l=len(myName)
if (l == 0):
	print ("You haven’t entered anything. \nPlease enter your full name.")
elif (l < 4):
	print ("You have entered less than 4 characters. \nPlease make sure that you have entered your name and surname.")
elif (l >= 25):
	print("You have entered more than 25 characters. \nPlease make sure that you have only entered your full name.")
else:
	print("Thank you for entering your name.")
	