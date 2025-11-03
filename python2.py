salaries=[]
l=int(input("enter:"))
for i in range(0,l):
    salary=int(input(f'salary {i+1}:'))
    salaries.append(salary)
if salaries[i]==2000:
    salaries.remove(i)
print(salaries)
