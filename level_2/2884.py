h,m = map(int,input().split())


if h<1:
    if m<45:
        print(23, m+15)
    else:
        print(0, m-45)
        
else:
    if m<45:
        print(h-1, m+15)
    else:
        print(h, m-45)
