N=int(input())

for i in range(N):
    an=list(input())

    score=0
    total=0

    for j in range(len(an)):
        if an[j]=='O':
            score=score+1
            total=total+score
        else :
            score=0

    print(total)
        
