n=int(input())
arr=[]
for i in range(n):
    li=list(map(int,input().split()))
    for i in li:
        arr.append(i)
arr.sort()
print(*arr)
