import math

print("Employee Database:")
print("...")

employeeList = {"001": ("Hester", 12), "002": ("Gavin", 34), "003": ("Kelsey", 9)
                }

spacer = str("\n\n\n\n\n")

while True:
    print("Options:")
    print("1 -  View All Employees\n2 - Modify Employee Data\n3 - Add New Employees\n4 - Search Database\n5 - Exit")
    print("...")
    menu = int(input("Enter: "))

    if menu == 5:
        break
    
    elif menu == 1:
        print("\n")
        print("ID Number: Employee Name")

        for key, value in employeeList.items():
            print("{}: {}".format(key, employeeList[key][0]))
            print("    Hours Worked: ", employeeList[key][1])
        
        print("...")
        any_key = input("Press any key to continue.\n")
        print(spacer)

    elif menu == 2:
        print("\n")
        print("Modify Existing Entry:")
        modID = str(input("Enter ID: "))
        print("Ok, this employee's name is: {}".format(employeeList[modID][0]))
        newName = str(input("Enter a New Name: "))
        newHW = int(input("How Many Hours Worked?: "))
        employeeList[modID] = (newName, newHW)
        print("\n")
        print("Employee ID#{} Entry Modified:".format(modID))
        print("Name: {}".format(newName))
        print("Hours Worked: {}".format(newHW))
        print("...")
        any_key = input("Press any key to continue.\n")
        print(spacer)

    elif menu == 3:
        print("\n")
        print("Create New Employee Entry:")
        name = str(input("Enter Employee Name: "))
        hw = int(input("Hours Worked: "))
        idNum = str(input("ID Number: "))
        employeeList[idNum] = (name, hw)
        print("\n")
        print("New Employee Entry Created:")
        print("{}: {} - {} Hours Worked".format(idNum, name, hw))
        print("...")
        any_key = input("Press any key to continue.\n")
        print(spacer)

    elif menu == 4:
        print("\n")
        print("Search Database By:")
        print("1 - Employee Name\n2 - Employee ID Number")
        searchMenu = int(input("Enter: "))

        if searchMenu == 1:
            print("This feature is not yet available.")
            print("\n")
        elif searchMenu == 2:
            print("This feature is not yet available.")
            print("\n")
        else:
            print("Unknown input. Please try again.")
            print("\n")

    else:
        print("Unknown input. Please try again.")
        print("\n")
        
        
        
        
    
