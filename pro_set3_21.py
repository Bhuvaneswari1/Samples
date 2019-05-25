n=int(input())
d=list(map(int,input().split()))
count=0
for i in range(1,len(d)):
    a=d[0:i]
    b=d[i:len(d)]
    if sum(a)//len(a)==sum(b)//len(b):
        count=count+1
        break
    
if count>0:
    print("yes")
else:
    print("no")
