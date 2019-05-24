n=int(input())
p=0
for i in range(0,n):
    c=n%10
    p=p+c
    n=n//10
s1=str(p)
c=s1[::-1]
if c==s1:
    print("YES")
else:
    print("NO")
