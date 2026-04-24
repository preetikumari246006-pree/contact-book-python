while True:
    print("Welcome In This tool")
    print("===== Contact Book =====")
    print("1. Add Contact ")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("1.Adding number......")
    elif choice == "2":
        print("2.Viewing contact.......")
    elif choice == "3":
        print("3.Searching contact.......")
    elif choice == "4":
        print("4.Deleting number.......")
    elif choice == "5":
        break
    else:
        print("Invalid choice! Enter 1-5")
