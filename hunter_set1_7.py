n=int(input())
a = [int(x) for x in input().split()]
for i in range(0,n):
    if (i%2==0):
        if a[i]%2!=0:
            print(a[i],end="")
    elif (i%2!=0):
        if a[i]%2==0:
            print(a[i],end="")
