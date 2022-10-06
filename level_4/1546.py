n=int(input())
score=list(map(int,input().split()))
m=max(score)
re=[]

for i in range(n):
    value=score.pop()
    value=value/m*100
    re.append(value)

avg=sum(re)/len(re)
print(avg)
