n=int(input())
l=list(map(int,input().split()))
desc_ord=[]
for i in l:
                s=bin(i)
                s1=s[2:]
                desc_ord.append(([s1.count("1"),i]))
	#print(l1)
desc_ord.sort(reverse=True)
for i in range(0,len(desc_ord)):
	print(desc_ord[i][1])
