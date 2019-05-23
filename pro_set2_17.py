n,k=map(int,input().split())
l1=list(map(int,input().split()))
count=0
for i in range(len(l1)):
    for j in range(i,len(l1)):
        if l1[i]+l1[j]==k:
            count=count+1
            break
if count>0:
    print("yes")
else:
    print("no")
