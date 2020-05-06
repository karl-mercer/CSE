import drink
import sandwich
import fries
import ketchup

"""
Program Description:
Combo menu program for CSE.
"""

total_cost = 0.0 #initialize total cost as a float type variable
order_list = ["", "", "", 0]
sandwich_pos = 0
drink_pos = 1
fries_pos = 2
ketchup_pos = 3

total_cost, order_list[sandwich_pos] = sandwich.choose_sandwich(total_cost)

total_cost, order_list[drink_pos] = drink.choose_drink(total_cost)

total_cost, order_list[fries_pos] = fries.order_fries(total_cost)

total_cost, order_list[ketchup_pos] = ketchup.packet_order(total_cost)

if beverage_size != "no" and fries_size != "no":
	total_cost -= 1.00

print("\nYour order includes a {} sandwich, {} drink, {} fry, and {} ketchup packets.".format(order_list[sandwich_pos], order_list[drink_pos], order_list[fries_pos], order_list[ketchup_pos]))
print("Your total cost is ${}. How would you like to pay?".format(total_cost))
