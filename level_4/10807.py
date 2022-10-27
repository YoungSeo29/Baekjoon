N=int(input())

num=[]
count=0

num=list(map(int,input().split()))

v=int(input())

for i in range(N):
    if num[i]==v:
        count=count+1

print(count)

        
