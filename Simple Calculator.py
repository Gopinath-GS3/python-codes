# This is the Python program for Simple Calculator Application
# This program designed with two options 
# Option 1:
#       In this option inputs are gathered from user.
#       The inputs are two numbers and arithmetic operation to perform
#       The calculation is performed and equation is diplayed
#       In the mean time, every equation entered by user is written in a text file.
# Option 2:
#       In this option user asked to enter text file name.
#       If the user enters, correct text file name means it will display the equations in the file
#       Otherwise, error handling is executed and error message is displayed.

import math     # Importing this module for performing arithmetic operations.
print("*** Simple Calculator ***\n")
print("Select you option from below list: ")
print("1. Enter the Inputs and Arithmetic Operation")
print("2. Read Equations from text file\n")
option = int(input("Enter your option (1 or 2): "))         # User option is assigned to variable 'option'

if option == 1:         
    while True: 
        try:
            number1 = int(input("\nEnter the number1: "))
            break 
        except ValueError:      # Error handling - This will return the below error message if user enters other then integer
            print("Oops! That was not a valid number. Try again...")
    while True: 
        try:
            number2 = int(input("Enter the number2: "))
            break 
        except ValueError:  # Error handling - This will return the below error message if user enters other then integer
            print("Oops! That was not a valid number. Try again...")

    operation_to_perform = input("Enter the Symbol for Operation to perform: ")         # Input for which arithmetic operation needs to be done

    if operation_to_perform == "+":     # Internal if..elif..else conditions to perform the arithmetic operation
        equation_output = number1 + number2
        line1 = ["Addition: " + str(number1) + "+" + str(number2) + "=" + str(round(equation_output))]
    elif operation_to_perform == "-":
        equation_output = number1 - number2
        line1 = ["Subtraction: " + str(number1) + "-" + str(number2) + "=" + str(round(equation_output))]
    elif operation_to_perform == "*":
        equation_output = number1 * number2
        line1 = ["Multiplication: " + str(number1) + "*" + str(number2) + "=" + str(round(equation_output))]
    elif operation_to_perform == "/":
        equation_output = number1 / number2
        module_output = number1 % number2
        if module_output >= 1:
            equation_output = round(equation_output, 2)
            line1 = ["Division: " + str(number1) + "/" + str(number2) + "=" + str(equation_output)]
        else:
            line1 = "Division: " + str(number1) + "/" + str(number2) + "=" + str(round(equation_output))
    else:
        print ("Enter a valid operation to perform + or - or * or /")

    print (line1)
    file1 = open ('sample.txt', 'a')        # This will open a text file 'sample.txt'
    file1.writelines(line1)         # This will write the equations returned by if..elif..else statement into the 'sample.txt' file
    file1.writelines('\n')      # This is for printing in new line in future

elif option == 2:
    print("\nGet text file and display the equations")
    filename = input("Enter the file name: ")       # Asks for which file name needs to open
    try:
        file2 = open(filename, "r")     
        line2 = file2.read()
        print(line2)        # Display the contents in the text file
    except FileNotFoundError as error:      # Error Handling - This will print the below error message if the file is not exist
        print("The file name entered is not exist")
        print(error)

else:
    print("Enter a valid option")