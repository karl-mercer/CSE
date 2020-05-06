def packet_order(total_cost):
	#packets variabl will record an integer for how much ketchup they order
	while True:
		packets = input("How many ketchup packets would you like?\n\n").strip()
		try:
			total_cost += float(packets)*.25
			break

		except ValueError:
			print("\nPlease enter an integer only.")

	return total_cost, packets