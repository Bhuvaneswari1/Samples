n, k=map(int, input().split())
arr1=[]
for _ in range(n):
	arr2 = set(map(int, input().split()))  
	arr1.append(arr2)
result=set.intersection(*arr1)
print(*result)
