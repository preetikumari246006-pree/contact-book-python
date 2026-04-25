contacts = []
while True:
    print("===== Contact Book =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter your name: ")
        num = input("Enter your number: ")
        contact = {"name": name, "number": num}
        contacts.append(contact)
        print("Contact saved Successfully...")
    elif choice == "2":
        if len(contacts) == 0:
                print("No contacts found!")
        else:
            for contact in contacts:
                print("Name:", contact["name"], "| Number:", contact["number"])
    elif choice == "3":
        print("3. Searching contact.......")
    elif choice == "4":
        print("4. Deleting number.......")
    elif choice == "5":
        break
    else:
        print("Invalid choice! Enter 1-5")
