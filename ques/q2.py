'''This code is for sum and avg of the give list '''
integer_num=list(map(int,input().split(",")))
total=0

"""for i in integer_num:
    total+=i
    avg=total/len(integer_num)
print(total, avg)"""

total, avg = sum(integer_num), sum(integer_num)/len(integer_num)
print(total, avg)

with open('numbers_data.txt','w') as output_file:
    output_file.write(f'list:{integer_num}\n')
    output_file.write(f'sum:{total}\t')
    output_file.write(f'avg:{avg}\n')
    output_file.close()
    
with open('numbers_data.txt','r') as input_file:
    file_list=input_file.readline()
    file_integer_sum_line=input_file.readline()
    file_integer_avg_line=input_file.readline()
    print(file_list)
    print(file_integer_sum_line)
    print(file_integer_avg_line)
