total=int(input())
n=int(input())
price=0

for i in range (1,n+1):
    price_i,num_i=map(int,input().split())
    price=price+price_i*num_i

if price==total:
    print("Yes")
else:
    print("No")
