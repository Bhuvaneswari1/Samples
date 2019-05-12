num=int(input())
steps=list(map(int,input().split()))
total=0
for i in range(1,len(steps)):
    for j in range(0,i):
        if(steps[j]<steps[i]):
            total+=steps[j]
print(total)
