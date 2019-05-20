n,k=map(int,input().split())
array1=[int(x) for x in input().split()]

count=1
for i in range(0,len(array1)-1):
    for j in range(i+1,len(array1)):
        if(array1[i]+array1[j]==k):
            count=0
if(count==0):
    print("YES")
else:
    print("NO")
