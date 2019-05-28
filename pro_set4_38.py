n,k=map(int,input().split())
list1=list(map(int,input().split()))
count=0
for i in list1:
	if i<=(5-k):
		count+=1
tot_team=count//3
print(tot_team)
