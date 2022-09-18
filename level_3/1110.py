num=int(input())
n=0
origin=num

while(True):
    if num<10:
        a=0
        num=num*10 + num
        n=n+1
    else :
        a=num//10
        b=num%10
        c=a+b
        num=b*10 + c%10
        n=n+1

    if origin == num:
        break
  
print(n)
