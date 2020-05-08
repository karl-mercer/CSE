import drink
import sandwich
import fries
import ketchup

"""
Program Description:
Combo menu program for CSE.
"""

total_cost = 0.0 #initialize total cost as a float type variable
order = [] #creates an empty list to remember the user's order

sandwich_choice = "no" 
beverage_size = "no" 
fries_size = "no" 
ketchup_quantity = 0 

total_cost, sandwich_choice = sandwich.choose_sandwich(total_cost)
order.append(sandwich_choice)

total_cost, beverage_size = drink.choose_drink(total_cost)
order.append(beverage_size)

total_cost, fries_size = fries.order_fries(total_cost)
order.append(fries_size)

total_cost, ketchup_quantity = ketchup.packet_order(total_cost)
order.append(ketchup_quantity)

if beverage_size != "no" and fries_size != "no":
	total_cost -= 1.00

print("\nYour order includes a {} sandwich, {} drink, {} fry, and {} ketchup packets.".format(order[0], order[1], order[2], order[3]))
print("Your total cost is ${}. How would you like to pay?".format(total_cost))