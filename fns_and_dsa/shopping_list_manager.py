def display_menu():
    print("shopping list manager")
    print("1. Add item")
    print("2, Remove item")
    print("3. view list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    shopping_list = []
    print("Welcome to the shopping list Manager")
    while True:
        display_menu()
        choice = input("Enter your choice:(1/2/3/4)")
        if choice == "1":
            item=input("Enter the item to add:")
            shopping_list.append(item)
            print(f""{item}" has been added to the shopping list")
        elif choice == "2":
            item = ("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f" "{item}" has been removed from the shopping list")
            else:
                print(f" "{item}" is not found in the shopping list")
            elif choice =="3":
                if shopping_list:
                    print("Here is your shopping list")
                    for index, item in enumerator(shopping_list, start=1):
                        print(f""{index}.{item}")
                        else:
                        print("Your shopping list is empty.")
                        elif choice =="4"
                        print("Thank you for using the shopping list manager. Goodbye!")
                        break
                        else:
                        print("invalid choice please enter a valid option(1/2/3/4.")
                        if_name_=="_main_":
                        main()
