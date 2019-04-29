import collections

n = int(input())
a1 = []
a2 = input().split()
for i in range(0,n):
	a1.append(a2[i])

result = collections.Counter(a1)
a3 = []
for i in result:
	if(result[i]==1):
		a3.append(i)
print(" ".join(a3))
