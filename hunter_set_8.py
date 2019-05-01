n=input()
a=list(map(int,input().split()))
for i in range(0,len(a)):
    for j in range(1,len(a)):
        for k in range(2,len(a)):
            if(i<j<k):
                if(a[i]+a[j]==a[k]):
                    print(a[i],end="")
                    print(a[j],end="")
                    print(a[k])
