s=input()
count=0
for i in range(0,len(s)):
    k=s[0:i]+s[i+1::]
    if k==k[::-1]:
        count=count+1
        break
if count!=0:
    print("YES")
else:
    print("NO")
