x,y=input().split()
x1=len(x)
y1=len(y)
if y1>x1:
    i=0
    while i<x1 and x[i]==y[i]:
        i+=1
    print(y1-i)
elif y1==x1:
    i=0
    while i<y1 and x[i]==y[i]:
        i+=1
    print(y1-i)
else:
    i=0
    while i<y1 and x[i]==y[i]:
        i+=1
    x2=x[i:]
    y2=y[i:]
    l=list(x2)
    z=0
    for c in y2:
        if c in l:
            z+=1
            l.remove(c)
    print(x1-i-z)
