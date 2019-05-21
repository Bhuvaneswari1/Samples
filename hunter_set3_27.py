x=input()
re=list(reversed(x))
b=''.join(re)
if(x==b):
    l = len(x)
    x = x[:l - 1]
    print(x)
else:
    print(x)
