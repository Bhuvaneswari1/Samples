n=int(input())
a1=list(map(int,input().split()))
b1=1
a,b=0,0
for i in range(0,len(a1)-1):
  for j in range(i+1,len(a1)):
    if abs(a1[i]+a1[j])<b1:
      a,b=a1[i],a1[j]
      b1=abs(a+b)
print(a,b)
