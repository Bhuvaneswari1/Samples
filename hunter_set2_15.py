num=int(input())
list1=list(map(int,input().split()))
star=[]
for i in range(0,num-1):
  if list1[i]>max(list1[i+1:]):
    star.append(list1[i])
star.append(list1[num-1])
print(*star)
print(max(list1))
