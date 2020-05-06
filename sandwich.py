def choose_sandwich(total_cost):
	print("Welcome to McSchnaars! What can I get for you today?")
	print("Chicken sandwich".ljust(25, '.')+"$5.25")
	print("Beef sandwich".ljust(25, '.')+"$6.25")
	print("Tofu sandwich".ljust(25, '.')+"$5.75\n")


	sandwich_list = ["chicken", "beef", "tofu"] #creating a list of sandwich choices
	sandwich_choice = "" #initialize choice to an empty string

	#loop that will run until the user make a valid sandwich choice
	while sandwich_choice not in sandwich_list:
		sandwich_choice = input("Enter your choice: ").strip().lower()
		if sandwich_choice not in sandwich_list:
			print("Sorry, we don't offer a {} sandwich.\n".format(sandwich_choice))
			print("Here are the sandwich choices we offer:\n\nChicken sandwich - $5.25 \nBeef sandwich - $6.25 \nTofu sandwich - $5.75\n")

	if sandwich_choice == "chicken":
		total_cost += 5.25
	elif sandwich_choice == "beef":
		total_cost += 6.25
	elif sandwich_choice == "tofu":
		total_cost += 5.75

	#statement that summarizes the user's order to this point	
	print("\nYou ordered a {} sandwich.\n".format(sandwich_choice))
	return total_cost, sandwich_choice