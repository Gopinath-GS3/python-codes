# This is a Python program using for Loop
# In this program we are going to print triangle like structure of "*"
# As per the instructions the program needs to print 5 rows of "*"
# Each row need to print that "*" of the row number


print("This is the program for ***for loop***")

# Option 1: Assigning input directly as per task instruction
no_of_rows = 5 
# option 2: Get input from user
# no_of_rows = int(input("Enter number of rows needed to print: "))

for row in range (no_of_rows + 1):    #outer loop
    no_of_iteration = row
    for no_of_iteration in range (row):   #inner loop
        print("*", end = '')    #Printing the * symbol in single line
        #no_of_iteration =+ 1
    print("")   #Print in new line
     
# Reference https://spiderlabweb.com/printing-triangle-patterns-python/

