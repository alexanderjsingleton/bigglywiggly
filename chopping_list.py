# Add help command.
# Add SHOW command.
# Clean code.



# make a shooping list to hold onto our items
shopping_list = []


def show_help():
	# print out instructions on how to use the app
	print("Whathu gonna have at the chopshop?")
	print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")

show_help()

while True:
	# ask for new items
	new_item = input("> ")

	# add new ites to our list
	shopping_list.append(new_item)

	if new_item == 'DONE':
		break
	elif new_item == 'HELP':
		show_help()
		continue

# be able to quit the app

# print out the list
print("Here's your list:")

for item in shopping_list:
	print(item)


