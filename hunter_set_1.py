import collections

n = int(input())
x = []
y = input().split()
for i in range(0,n):
	x.append(y[i])

result = collections.Counter(a)
z = []
for i in result:
	if(result[i]>1):
		z.append(i)
c = sorted(c)
if not c:
	print("unique")
else:
	print(" ".join(z))
