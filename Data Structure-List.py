# This is a Python program for List Data Structure
# In this program we have to do calculations using List and Dictionary data structures
# 1. Create a list called Menu with some items for a Cafe
# 2. Create separate dictionary named Price and Stock for each items in Menu list
# 3. Multiply the Price and Stock values to get the total_stock value in the Cafe
# 4. Display the total_stock value

print("\n*** This is the program for List Data Structure ***")
print("\nWelcome to CAFE\n")
menu = ['Coffee', 'Soup', 'Cupcake', 'Muffin']      # Menu list for items
length = len(menu)
stock_dictionary = {'Coffee':25, 'Soup':15, 'Cupcake':60, 'Muffin':45}      # Stock Dictionary for stock details of each item
price_dictionary = {'Coffee':2.5, 'Soup':3.5, 'Cupcake':1.0, 'Muffin':1.5}  # Price Dictionary for price of each item
total_stock = 0
item_value = []     # New list to store the total value of each item
for item in menu:   # For loop will run until each item in Menu list is iterated
    value = stock_dictionary[item] * price_dictionary[item]
    item_value.append(value)        # Each items total value is appended in item_value List
    total_stock += value    # This is for total stock in the cafe
print("ITEM\t\tSTOCK\tPRICE(£)\tITEM_VALUE(£)")

i=0
for item in menu:       # This for loop is for printing all the menu items with the Stock, price and item_value details
    print(menu[i] + "\t\t" + str(stock_dictionary[item]) + "\t" + str(price_dictionary[item]) + "\t\t" + str(item_value[i]))
    i += 1
print(f"\nTotal Stock value in the CAFE is £{total_stock}\n") # This print() displays total stock value of cafe

