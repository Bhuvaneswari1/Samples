n,k=map(int,input().split())
list1=list(map(int,input().split()))
if k==1:
  print(min(list1))
elif k==2:
  print(max(list1[0],list1[n-1]))
else:
  print(max(list1))
