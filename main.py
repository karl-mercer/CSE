import drink
import sandwich
import fries
import ketchup

"""
Program Description:
Combo menu program for CSE.
"""

total_cost = 0.0 #initialize total cost as a float type variable
sandwich_choice = "no"
beverage_size = "no"
fries_size = "no"
ketchup_quantity = 0

total_cost, sandwich_choice = sandwich.choose_sandwich(total_cost)

total_cost, beverage_size = drink.choose_drink(total_cost)

total_cost, fries_size = fries.order_fries(total_cost)

total_cost, ketchup_quantity = ketchup.packet_order(total_cost)

if beverage_size != "no" and fries_size != "no":
	total_cost -= 1.00

print("\nYour order includes a {} sandwich, {} drink, {} fry, and {} ketchup packets.".format(sandwich_choice, beverage_size, fries_size, ketchup_quantity))
print("Your total cost is ${}. How would you like to pay?".format(total_cost))
print("Thank you for your business. Have a nice day!")