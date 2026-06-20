# Initialize data structures
my_list = []
my_tuple = ()
my_set = set()
my_dict = {}

# Display Function
def display():
    print("\n----- Current Data -----")
    print("List      :", my_list)
    print("Tuple     :", my_tuple)
    print("Set       :", my_set)
    print("Dictionary:", my_dict)

while True:
    print("\n===== MENU =====")
    print("1. Insert")
    print("2. Update")
    print("3. Delete")
    print("4. Display")
    print("5. Sort List")
    print("6. Search")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # Insert
    if choice == 1:
        val = input("Enter value to insert: ")

        my_list.append(val)
        my_set.add(val)

        key = input("Enter key for dictionary: ")
        my_dict[key] = val

        my_tuple = my_tuple + (val,)

        print("Inserted Successfully!")

    # Update
    elif choice == 2:
        old = input("Enter value to update: ")
        new = input("Enter new value: ")

        if old in my_list:
            index = my_list.index(old)
            my_list[index] = new

        if old in my_set:
            my_set.remove(old)
            my_set.add(new)

        my_tuple = tuple(new if x == old else x for x in my_tuple)

        for k in my_dict:
            if my_dict[k] == old:
                my_dict[k] = new

        print("Updated Successfully!")

    # Delete
    elif choice == 3:
        val = input("Enter value to delete: ")

        if val in my_list:
            my_list.remove(val)

        if val in my_set:
            my_set.remove(val)

        my_tuple = tuple(x for x in my_tuple if x != val)

        keys_to_delete = [k for k, v in my_dict.items() if v == val]

        for k in keys_to_delete:
            del my_dict[k]

        print("Deleted Successfully!")

    # Display
    elif choice == 4:
        display()

    # Sort
    elif choice == 5:
        my_list.sort()
        print("Sorted List:", my_list)

    # Search
    elif choice == 6:
        val = input("Enter value to search: ")

        print("In List      :", val in my_list)
        print("In Set       :", val in my_set)
        print("In Dictionary:", val in my_dict.values())
        print("In Tuple     :", val in my_tuple)

    # Exit
    elif choice == 7:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Try Again.")