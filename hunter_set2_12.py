a,b=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
l.reverse()
for idx,val in enumerate(l):
    if(idx==b-1):
        print(val)
        break
