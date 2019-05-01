n = int(input())
a = input().split()
count=0
for i in range(0,n):
    for j in range(i+1,n):
      if(a[i]==a[j]):
        print(a[i])
        count=1
      if(count==1):
        break
      else:
        continue
