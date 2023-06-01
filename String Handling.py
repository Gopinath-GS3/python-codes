# This is a Python Program for String Handling
# In this program, we are going to perform below operations.
#   1. Converting each alternate characters in a string to Uppercase and Lowercase alternatively.
#       Ex: “Hello World” would become “HeLlO WoRlD”
#   2. Converting each words in a string to Lowercase and uppercase alternatively.
#       Ex: “I am learning to code” would become “i AM learning TO code”)
# This program is designed to do string handling with user entered input.

print("***Program for String Handling***")
print("Select you option from below list: ")
print("1. Converting Alternate Characters")
print("2. Converting Alternate Words")
print("3. Exit")
option = int(input("Enter your option number: ")) # Asking option from User, whether they want to convert alternative characters or words

while option != 3:      # While loop to run the program until user enters Option 3

    if option == 1:     # If User selects option 1 means If statement will be executed 
        print("\n1. Converting Alternate Characters")
        sentence1 = input("Enter the sentence: ")       # Asks for user input
        print("User Input word/Sentence: \t" + sentence1)
        str_length = len(sentence1)
        i = 0
        print("Case converted Characters: \t", end="")      # the parameter end="" used to print the output from different print() in same line
        while i < str_length:
            if i%2 !=0:
                print(sentence1[i].lower(), end="")
            else:
                print(sentence1[i].upper(), end="")
            i += 1
        print('\n') # The new line comment is used to start printing in new line

    elif option == 2:   # If User selects option 2 means else statement will be executed
        print("\n2. Converting Alternate Words")
        sentence1 = input("Enter the sentence: ")   # Asks for user input
        print("Original Sentence: \t" + sentence1)
        split_sen1 = sentence1.split(" ")   # split() function is used to divide the sentence into words and saved as a new list for string manipulating
        case_conversion = []
        new_string = " "
        i=1
        for iteration in split_sen1:
            if i%2 != 0:
                new_string = iteration.lower()
            else:
                new_string = iteration.upper()
            case_conversion.append(new_string)  # append() function will add the current string to the end of the mentioned list name
            i+=1
        altered_sentence= " ".join(case_conversion) # the list items are joined by the parameter used in join() function
        print("Converted words: \t" + altered_sentence)

    else:       # If User not enter the number in options, then the else statement will be executed
        print("Enter a valid option")

    print("\nSelect you option from below list: ")      # This program will run, until user wants to exit from the cycle
    print("1. Converting Alternate Characters")
    print("2. Converting Alternate Words")
    print("3. Exit\n")
    option = int(input("Enter your option number: ")) 

print("The String Handling program is Exited")  # Program will end with print this statement, if user enter option3

