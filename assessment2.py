#Employees code using CRUD operations

employees = []  

def add_employee():
    id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    designation = input("Enter Employee Designation: ")
    salary = float(input("Enter Employee Salary: "))
    employee = (id, name, designation, salary)
    employees.append(employee)
    print("Employee Added Successfully!\n")

def search_employee():
    id = int(input("Enter Employee ID to Search: "))
    for emp in employees:
        if emp[0] == id:
            print(f"Employee Found: ID={emp[0]}, Name={emp[1]}, Designation={emp[2]}, Salary={emp[3]}\n")
            return
    print("Employee Not Found.\n")

def update_employee():
    id = int(input("Enter Employee ID to Update: "))
    for i in range(len(employees)):
        if employees[i][0] == id:
            new_salary = float(input("Enter New Salary: "))
            emp = employees[i]
            employees[i] = (emp[0], emp[1], emp[2], new_salary)  # create updated tuple
            print("Employee Updated Successfully!\n")
            return
    print("Employee Not Found.\n")

def delete_employee():
    id = int(input("Enter Employee ID to Delete: "))
    for i in range(len(employees)):
        if employees[i][0] == id:
            employees.pop(i)
            print("Employee Deleted Successfully!\n")
            return
    print("Employee Not Found.\n")

def display_employees():
    if employees:
        print("\nAll Employees:")
        for emp in employees:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Designation: {emp[2]}, Salary: {emp[3]}")
        print()
    else:
        print("\n Employees Found.\n")

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