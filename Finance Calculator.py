# Python Program using if-elif-else statements for calculating Interest for deposit and Loan repayment
# This program includes the importing math function
# Intially provide menu and ask for user's input
# Regarding the option selected by user, get the details needed for calculation from user using input()
# Then do the calculation and print the output
# Basically the interest and loan repayment calculations returns floating value as output.
# So we use round() to print the floating output to near Integer value. 

import math
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
option = option.lower() #The input is converted into lowercase to avoid Case difference between Input and value assigned condition statement

if option == "investment":
    print("\n***INVESTMENT CALCULATOR***")
    principle = int(input("\nEnter the amount that you are depositing: "))
    interest_rate = int(input("Enter the interest rate: "))
    interest_rate = interest_rate / 100
    no_of_years = int(input("Enter how many years planned to invest: "))
    interest = input("\nEnter the interest type you like to invest, either'simple' or 'compound: ")
    interest = interest.lower() #The input is converted into lowercase to avoid Case difference between Input and value assigned condition statement
    
    if  interest == "simple":
        simple_interest = principle * (1 + interest_rate*no_of_years)
        print("\nTotal amount after applying Interest: {}".format(round(simple_interest)))
    elif interest == "compound":
        compound_interest = principle * math.pow ((1 + interest_rate), no_of_years)
        print("\nTotal amount after applying Interest: {}".format(round(compound_interest)))
    else:
        print("\nEnter a valid option")

elif option == "bond":
    print("\n***HOUSE LOAN REPAYMENT CALCULATOR***")
    loan_principle = int(input("\nEnter the current value of the house: "))
    annual_interest = int(input("Enter the annual interest rate: "))
    interest_per_month = (annual_interest/100) / 12
    repay_months = int(input("Enter how many months planned to repay: "))
    repayment_amount = (interest_per_month * loan_principle)/(1 - (1 + interest_per_month)**(-repay_months))
    print("\nMontly repayment amount: {}".format(round(repayment_amount)))

else:
    print("Enter a valid option")