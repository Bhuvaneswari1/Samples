n,m=map(int,input().split())
l1=list(map(int,input().split()))
arr=[]
s=0
for i in range(m):
    u,v=map(int,input().split())
    s=0
    for j in range(u-1,v):
        s=s^l1[j]
        #print(s)
    arr.append(s)
        
for i in range(len(arr)):
    print(arr[i])
