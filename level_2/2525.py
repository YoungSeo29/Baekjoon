h,m=map(int,input().split())
t=int(input())

m=m+t

h=h+m//60
m=m%60

if h==24:
    h=0
elif h>24:
    h=h-24

if m>60:
    print(h+1, m-60)
else:
    print(h, m)
