n=int(input())
array1=list(map(int,input().split()))
product=1
result=[]
for i in array1:
  product=product*i
for i in array1:
  result.append(product//i)
print(*result)
