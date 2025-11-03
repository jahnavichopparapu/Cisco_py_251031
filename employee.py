employees=[]

def add_emlopyee(employee):
    employees.append(employee)
def search_employee(id):
    i=0
    for employee in employees:
        if employee[0]==id:
            return i
        i+=1
    return -1
def update_emp(id,salary):
    index=search_employee(id)
    