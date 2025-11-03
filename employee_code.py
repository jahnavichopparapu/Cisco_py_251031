employees = {}  

def add_employee(id, name, designation, salary):
    employees[id] = {
        'name': name,
        'designation': designation,
        'salary': salary
    }
    print('Employee Added Successfully')

def search_employee(id):
    if id in employees:
        return employees[id]
    else:
        return None

def update_employee(id, salary):
    if id in employees:
        employees[id]['salary'] = salary
        print('Employee Updated Successfully')
    else:
        print('Employee Not Found.')

def delete_employee(id):
    if id in employees:
        del employees[id]
        print('Employee Deleted Successfully')
    else:
        print('Employee Not Found.')

add_employee(101, 'Pratik', 'Software Engineer', 56000)
add_employee(102, 'Abhishek', 'Software Automation Engineer', 40000)
add_employee(103, 'Rishabh', 'Software Automation Engineer', 99000)
add_employee(104, 'Nihar', 'Software Automation Engineer', 99)
add_employee(105, 'Divya', 'Business Analyst', 45000)

print("\nAll Employees:")
for id, details in employees.items():
    print(id, details)

emp = search_employee(104)
if emp:
    print('\nSearched Employee:', emp)
else:
    print('\nEmployee Not Found.')

update_employee(104, 99200)
print("\nAfter Update:")
for id, details in employees.items():
    print(id, details)

add_employee(106, 'Mahesh', 'Python Trainer', 4200)
print("\nAfter Adding New Employee:")
for id, details in employees.items():
    print(id, details)

delete_employee(106)
print("\nAfter Deletion:")
for id, details in employees.items():
    print(id, details)
