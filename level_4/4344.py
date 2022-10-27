c=int(input())

for i in range(c):
    total=0
    average=0
    over=0
    
    score=list(map(int,input().split()))
    num=score[0]

    for j in range(1, len(score)):
        total=total+score[j]

    average=total/num

    for j in range(1,len(score)):
        if score[j]>average:
            over=over+1

    rate=over/num*100
    print(f'{rate:.3f}%')

