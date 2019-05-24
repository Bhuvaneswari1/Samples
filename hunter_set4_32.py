n=int(input())
l=list(map(int,input().split()))
evenpos=l
while len(l)>1:
	l=l[1::2]
	#print(l)
print(evenpos.index(l[0]))
