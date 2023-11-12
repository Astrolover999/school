list1 = [int(i) for i in input().split()]
if len(list1) == 1:
    print(list1[0])
elif len(list1) == 2:
    print(list1[1]*2, list1[0]*2)
else:
    for i in range(len(list1)):
        if i < len(list1) - 1:
            print(list1[i-1] + list1[i+1], end=" " )
        else:
            print(list1[0] + list1[i-1])