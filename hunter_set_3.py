n = int(input())
a1 = []
a2 = input().split()
for i in range(0,n):
	a1.append(int(a2[i]))

a3 = []
for i in range(0,n):
	if(i == a1[i]):
		a3.append(str(a1[i]))
if not a3:
	print("-1")
else:
	a3 = sorted(a3)
	print(" ".join(a3))
