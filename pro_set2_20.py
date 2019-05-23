n,s=map(int,input().split())
v1=list(map(int,input().split()))
v1.sort(reverse=True)
count=0
for i in range(0,len(v1)):
    if s>=v1[i]:
        count=count+s//v1[i]
    s=s%v1[i]
    if s==0:
        break
print(count)
