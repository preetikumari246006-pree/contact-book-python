import json

def load_contacts():
    try:
        file = open("contacts.json", "r")
        contacts = json.load(file)
        file.close()
        return contacts
    except:
        return []

def save_contacts():
    file = open("contacts.json", "w")
    json.dump(contacts, file)
    file.close()


contacts = load_contacts()
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
        print("Contact saved Successfully..")
        save_contacts()
    elif choice == "2":
        if len(contacts) == 0:
                print("No contacts found!")
        else:
            for contact in contacts:
                print("Name:", contact["name"], "| Number:", contact["number"])
    elif choice == "3":
        search = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact["name"] == search:
                print("Name:", contact["name"], "| Number:", contact["number"])
                found = True
        if found == False:
            print("Contact not found!")
    elif choice == "4":
        name = input("Enter name to delete: ")
        found = False
        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                save_contacts()
                found = True
        if found == False:
            print("Contact not found!")
    elif choice == "5":
        break
    else:
        print("Invalid choice! Enter 1-5")
