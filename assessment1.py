#Employees code using dictionary and CRUD operations

employees = {} 

def add_employee():
    id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    designation = input("Enter Employee Designation: ")
    salary = float(input("Enter Employee Salary: "))
    employees[id] = {
        'name': name,
        'designation': designation,
        'salary': salary
    }
    print("Employee Added Successfully!\n")

def search_employee():
    id = int(input("Enter Employee ID to Search: "))
    if id in employees:
        print(f"Employee Found: {employees[id]}\n")
    else:
        print("Employee Not Found.\n")

def update_employee():
    id = int(input("Enter Employee ID to Update: "))
    if id in employees:
        salary = float(input("Enter New Salary: "))
        employees[id]['salary'] = salary
        print("Employee Updated Successfully!\n")
    else:
        print("Employee Not Found.\n")

def delete_employee():
    id = int(input("Enter Employee ID to Delete: "))
    if id in employees:
        del employees[id]
        print("Employee Deleted Successfully!\n")
    else:
        print("Employee Not Found.\n")

def display_employees():
    if employees:
        print("\n All Employees:")
        for id, details in employees.items():
            print(f"ID: {id}, Name: {details['name']}, Designation: {details['designation']}, Salary: {details['salary']}")
        print()
    else:
        print("\n No Employees Found.\n")

while True:
    print("========= Employee Management System =========")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Display All Employees")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        search_employee()
    elif choice == '3':
        update_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        display_employees()
    elif choice == '6':
        print("Exiting Program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")