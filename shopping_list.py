# make a shooping list to hold onto our items
shopping_list = []

# print out instructions on how to use the app
print("Whathu gonna have at the chopshop?")
print("Enter 'CHOPPED' to stop adding items.")

while True:
	# ask for new items
	new_item = input("> ")

	# add new ites to our list
	shopping_list.append(new_item)

	if new_item == 'DONE':
		break

# be able to quit the app

# print out the list
print("Here's your list:")

for item in shopping_list:
	print(item)