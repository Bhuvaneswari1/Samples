n,m=map(int,input().split())
arr=[]
temp=0
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    arr[i].sort()
    #print(arr[i])
for D2 in range(n+m):
    for i in range(m):
        for j in range(n-1):
            if arr[j][i]>arr[j+1][i]:
                temp=arr[j][i]
                arr[j][i]=arr[j+1][i]
                arr[j+1][i]=temp
for i in range(n):
    print(*arr[i])

