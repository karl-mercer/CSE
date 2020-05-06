def choose_drink(total_cost):
	drink_sizes = ["small", "medium", "large", "no"]
	drink_choice = ""

	while drink_choice not in drink_sizes:
		drink_choice = input("Would you like a beverage? (yes or no)\n\n").strip().lower()
		if drink_choice == "yes":
			while drink_choice not in drink_sizes:
				print("\nWhat size beverage would you like?\n\n"+"Small".ljust(15, '.')+"$1.00\n"+"Medium".ljust(15, '.')+"$1.75\n"+"Large".ljust(15, '.')+"$2.25\n\n")
				drink_choice = input("Enter your choice: ")
				if drink_choice not in drink_sizes:
					print("Sorry, we don't offer a {} drink size.".format(drink_choice))
		elif drink_choice == "no":
			pass
		else:
			print("Sorry, I'm not sure what you mean.")

	if drink_choice == "small":
		total_cost += 2.00
		drink_choice = "a small"
	elif drink_choice == "medium":
		total_cost += 2.75
		drink_choice = "a medium"
	elif drink_choice == "large":
		total_cost += 3.25
		drink_choice = "a large"

	#statement that summarizes the user's order to this point	
	print("\nYou ordered {} drink.\n".format(drink_choice))
	return total_cost, drink_choice