ds=input()
for i in range(0,len(ds)):
    if ds[:i]==ds[i+1:]:
        
        count=0
        break
    else:
        count=1
if count==0:
    print("YES")
else:
    print("NO")
