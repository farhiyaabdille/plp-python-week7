shopping_list = []

while True:
    command = input("add / remove / show / done: ").strip().lower()

    if command == "add":
        item = input("Item to add: ").strip()
        shopping_list.append(item)
        print(f"Added: {item}")
    elif command == "remove":
        item = input("Item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed: {item}")
        else:
            print("That item is not on your list.")
    elif command == "show":
        if shopping_list:
            for item in shopping_list:
                print(item)
        else:
            print("Your list is empty.")
    elif command == "done":
        print("Goodbye!")
        break
    else:
        print("Please choose add, remove, show, or done.")
