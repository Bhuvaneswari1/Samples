n,m = input().split()
a = set(map(int,input().split()))
b = set(map(int,input().split()))
if(b.issubset(a)):
	print("YES")
else:
	print("NO")
