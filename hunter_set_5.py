n=input()
count=1
for i in range(len(n)-1):
	a=n[i]+n[i+1]
	x=int(a)
	if x<=26 and n[i]!="0":
		count+=1
if count==3:
	print(count)
else:
	print(count+(count-1)//2)
