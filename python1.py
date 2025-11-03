age=list(map(int,input().split(" ")))
min_age=age[0]
ages=0
for i in range(1,len(age)):
    ages=age[i]
    if min_age>ages:
        min_age=ages
print(min_age)