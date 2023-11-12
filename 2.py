a= [int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
elif len(a) == 2:
    print(a[1]*2, a[0]*2)
else:
    for i in range(len(a)):
        if i < len(a) - 1:
            print(a[i-1] + a[i+1], end=" " )
        else:
            print(a[0] + a[i-1])
