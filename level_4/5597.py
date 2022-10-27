std=[]
num=[]
for i in range(28):
    std.append(int(input()))

for i in range(1,31):
    num.append(int(i))

a=set(std)
b=set(num)

c=list(b-a)
c.sort()
print(c[0])
print(c[1])
