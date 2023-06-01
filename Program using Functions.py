# This is a program for using functions
# In this program we are going to define functions and using them in program
# As per the task instructions, we are going to create 3 separate functions which accepts parameters from program to execute them.
# One final function, which accepts functions as parameter and retuens the output.
# This program is designed to calculate holiday scenerio of calculating whole trip expenses
# The expenses includes Flight fare, Hotel bills and Car rentals
# The user provided with options of destinations, hotal and car types
# They have to select from the given options
# Then seprate functions are called and the fares are displayed.
# Finally the total fare is calculated by calling all the functions as parameters.
 
import math

def hotel_cost(hotel, nights): # Defining function hotel_cost() for calculating the hotel bill based on hotel type and number of nights stay
    if hotel==1:
        rent = 120
    elif hotel==2:
        rent = 100
    elif hotel==3:
        rent = 85
    elif hotel==4:
        rent = 70
    elif hotel==5:
        rent = 50
    else:
        print("Enter the correct value for destination parameter of hotel_cost()")
    hotel_bill = rent * nights
    return hotel_bill

def car_rental(car, rent_days):  # Defining car_rental() for calculating the car bill based on car type and number of days
    if car==1:
        rent_per_day = 30
    elif car==2:
        rent_per_day = 25
    elif car==3:
        rent_per_day = 40
    elif car==4:
        rent_per_day = 50
    elif car==5:
        rent_per_day = 35
    else:
        print("Enter the correct value for destination parameter of car_rental()")
    rental_bill = rent_per_day * rent_days
    return rental_bill

def plane_cost(destination): # Defining function plane_cost() for calculating the ticket fare based on destination
    if destination==1:
        ticket_rate = 86
    elif destination==2:
        ticket_rate = 50
    elif destination==3:
        ticket_rate = 46
    elif destination==4:
        ticket_rate = 30
    elif destination==5:
        ticket_rate = 98
    else:
        print("Enter the correct value for destination parameter of plane_cost()")
    flight_fare = ticket_rate * 2
    return flight_fare

def holiday_cost(pc, hc, cr):
    total_cost = pc + hc+ cr
    return total_cost

print("\n*** Program for Calculating Holiday Expenses***")

print("\nPlane Cost (One-way)")
print("1. Scotland\t: £86 \n2. London\t: £50\n3. Wales\t: £46 \n4. Manchester\t: £30 \n5. Ireland:\t: £98")
city_flight = int(input("Enter the Destination: "))   # User needs to enter destination from options

print("\nHotel cost (per night)")
print("1. 5 Star\t: £120 \n2. 4 Star\t: £100\n3. 3 Star\t: £85 \n4. Luxury\t: £70 \n5. Budget:\t: £50")
hotel_type = int(input("Enter the Hotel type: "))    # User needs to enter Hotel type from options
num_nights = int(input("Enter no.of.nights to stay: ")) # User needs to enter no.of.nights going to stay

print("\nRental Car cost (per day)")
print("1. Coupe\t: £30 \n2. Supermini\t: £25\n3. SUV\t\t: £40 \n4. Sports\t: £50 \n5. Sedan:\t: £35")
car_type = int(input("Enter the Car type: "))   # User needs to enter car type from options
rental_days = int(input("Enter no.of.days to hiring car: "))  # User needs to enter no.of.days car needed for rent

print("\nFlight Cost\t\t: £" +str(plane_cost(city_flight))) # This function returns Ticket Fare
print("Hotel Cost\t\t: £" +str(hotel_cost(hotel_type, num_nights))) # This function returns Hotel Bill
print("Car Rental Cost\t\t: £" +str(car_rental(car_type, rental_days))) # This function returns Car rental bill
print("Total Holiday Expenses\t: £" + str(holiday_cost(plane_cost(city_flight), hotel_cost(hotel_type, num_nights), car_rental(car_type, rental_days))))
    # This function takes all other 3 functions as parameter and retuens total expenses

# End of Program


