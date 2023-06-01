# This is a Python program using While Loop
# In this program we get inputs from User
# calculate the average of the collected integers and display the output.
# As per task instruction the program will request for input until the user enters -1.
# option 1: While loop will be exits, when user enter the value -1 
    # while (i != -1):
    # This loop takes negative value for calculating the average
# option 2: While loop will be exits, when user enters any negative number
    # while (i >= 0): 
    # This loop does not takes negative value for calculating the average
# This both options will gives different outputs.


print("This is the program for ***while loop***")

i = int(input("Enter a number: "))
sum = 0     # Variable to hold the total sum of numbers entered
n = 0   # Variable to hold no.of.inputs entered

while (i != -1): #option 1 is used here
    sum += i   # equivalent to sum = sum + 1
    n += 1   # equivalent to n = n + 1
    i = int(input("Enter a number: "))

avg = sum / n   # calculating the average
print ("Average for total sum of numbers entered is {}".format(round(avg)))  # round() used to print the output in near integer value of float type