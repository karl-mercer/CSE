def order_fries(total_cost):
	size_options = ["small", "medium", "large", "mega-size", "no"]
	size_choice = ""

	while size_choice not in size_options:	
		size_choice = input("Would you like fries today? (yes or no)\n\n").strip().lower()
		if size_choice == "yes":
			print("\nWhat size fries would you like?\n\n"+"Small".ljust(15, '.')+"$1.00\n"+"Medium".ljust(15, '.')+"$1.50\n"+"Large".ljust(15, '.')+"$2.00\n\n")
			size_choice = input("Enter your choice: ")
			if size_choice == "small":
				mega_size = "" #initialize mega_size to an empty string
				while mega_size not in ["yes", "no"]:
					mega_size = input("\nWould you like to Mega-Size your fries? (yes or no)\n\n").strip().lower()
		elif size_choice == "no":
			pass
		else:
			print("\nSorry, not sure I caught that.\n")

	if size_choice == "small":
		if mega_size == "yes":
			size_choice = "a mega-size"
		else:
			size_choice = "a small"
		total_cost += 1.00
	elif size_choice == "medium":
		total_cost += 1.50
		size_choice = "a medium"
	elif size_choice == "large":
		total_cost += 2.00
		size_choice = "a large"


	print("\nYou ordered {} fry. This is bad for your health...".format(size_choice))
	return total_cost, size_choice