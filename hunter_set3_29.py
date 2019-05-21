n=int(input())
l=list(map(int,input().split()))
post_num=[]
for i in range(n-1):
	for j in range(i,n):
		c=l[i:j+1]
		post_num.append(sum(c))
print(max(post_num))
