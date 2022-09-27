n_list=[]
for i in range(9):
    value=int(input())
    n_list.append(value)

max=n_list[0]
max_num=0
for i in range(8):
    if n_list[i+1]>max :
        max=n_list[i+1]
        max_num=i+1

print(max)
print(max_num+1)


