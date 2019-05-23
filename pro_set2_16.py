n=int(input())
k=list(map(int,input().split()))
candy=[]
candy=[1]*n
for i in range(n):
    if i==0:
        if k[i]>k[i+1]:
            candy[i]=candy[i]+candy[i+1]
    elif i>0:
        if k[i]>k[i-1]:
            candy[i]=candy[i]+candy[i-1]
            #print(s[i])
print(sum(candy))
