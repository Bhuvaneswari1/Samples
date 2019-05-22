n,q=map(int,input().split())
z=list(map(int,input().split()))
arr=[]
for i in range(q):
    u,v=map(int,input().split())
    arr.append(min(z[u-1:v]))
for i in range(len(arr)):
    print(arr[i])
