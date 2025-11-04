# minmax_data
list_input=list(map(int,input().split(",")))
min_num=list_input[0]
max_num=list_input[0]
for i in list_input:
    if min_num>i:
        min_num=i
    if max_num<i:
        max_num=i
print(min_num)
print(max_num)
