n=int(input())
l=list(map(int,input().split()))
x=0
y=0
for i in range(0,n):
	if i%2==0:
		x=x+l[i]
	else:
	  y=y+l[i]
if x>y:
	print(x)
else:
	print(y)
