# make a shooping list to hold onto our items
shopping_list = []

# print out instructions on how to use the app
print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")

while True:
	# ask for new items
	new_item = input("> ")

	if new_item == 'DONE':
		break


	# add new ites to our list
	shopping_list.append(new_item)

# be able to quit the app
# print out the listls