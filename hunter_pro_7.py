N=int(input())
b=1
Sqrt=2
while Sqrt<=N:
    if 2**b==N:
        b=0
        break
    else:
        Sqrt=2*b
        b=b+1
if(b!=0):
    result=Sqrt-N
    print(result)
else:
    print(0)
