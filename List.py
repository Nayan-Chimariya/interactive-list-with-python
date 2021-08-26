# simple list program

'''

commands: 
1. help
2. add 
3. remove
4. check index
5. max value
6. min value
7. clear list
8. arrange list
9. revome duplicate items 
10. exit program

'''

list = []

state_clear = False

while True:
  command = input("> ").lower()
  if command == "help":
    print(
      "\nThese are my commands: \n"
      "1. view - displays the current list\n"
      "2. add - adds number to the list: \n"
      "3. remove - removes number from the list\n"
      "4. check index - returns the index of the number\n"
      "5. max - returns the max value from the list\n"
      "6. min - returns the min value from the list\n"
      "7. clear - clears the list\n"
      "8. arrange - asks the user for the type of arrangement and does accordingly\n"
      "9. remove duplicate numbers from list\n"
      "10. exit - exits the program\n"
    )

  elif command == "view":
    print(f"\nList: {list}\n")
  
  elif command == "add":
    value_range = int(input("how many numbers do you want to add: "))
    s = 1 
    while s <= value_range:
      added = int(input(f"| {s} |Enter the value to add to the list: "))
      s += 1
      list.append(added)

    print(
      "\n✅ number were added\n"
      "the new list is\n"
      f"{list}\n"
    )
  
  elif command == "remove":
    removed = int(input("\nEnter the value to remove from the list: "))
    list.remove(removed)
    print(
      "✅ number was removed\n"
      "the new list is\n"
      f"{list}\n"
    )

  elif command == "remove duplicate":
    unique_list = []
    previous_list = list.copy()
    for duplicates in list: 
      if duplicates not in unique_list:
        unique_list.append(duplicates)
    list.clear()
    list = unique_list
    
    print(
      "\n✅ duplicated were removed\n"
      f"previous list = {previous_list}\n"
      "the new list is\n"
      f"{list}\n"
    )

  elif command == "arrange":
    type_of_arrangement = input(
      "\nenter\n" 
      "a for assending\n"
      "d for descending: "  
    ).lower()

    if type_of_arrangement == "a":
      list.sort()
      print("\n✅ list was sorted in ascending order\n")
      print(f"{list}\n")
      continue
    
    elif type_of_arrangement == "d":
      list.sort()
      list.reverse()
      print("\n✅ list was sorted in descending order\n")
      print(f"{list}\n")
      continue

    else:
      print("\n❗ Invalid choice\n")
      continue

  elif command == "index":
    chk_index = int(input("\nEnter the value to see the index of: "))
    found = list.index(chk_index)
    print(
      f"\n🔍 Search Result:\n "
      f"First {chk_index} was found in index [{found}]\n"
    )
  
  elif command == "max":
    if state_clear == True:
      print("\n❗ The list is empty\n")
      continue
    else:
      print(f"\nMAX: {max(list)}\n")
  
  elif command == "min":
    if state_clear == True:
      print("\n❗ The list is empty\n")
      continue
    else:
      print(f"\nMIN: {min(list)}\n")

  elif command == "clear":
    list.clear()
    state_clear = True
    print(
      "\n✅ List is now cleared\n"
      f"the new list is {list}\n"
    )
  
  elif command == "exit":
    break

  else:
    print(
      "\n⚠ no such commands was found\n"
      "----------------------------\n"
      "Check your spelling\n"
      "DO NOT add space after command\n"
      'Type "help" to see my commands list\n'
    )