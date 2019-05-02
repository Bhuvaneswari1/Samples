x,y=input().split()
result=0
if len(x)>len(y):
    #print("Yes")
    x,y=y,x
z=0
while z<len(x):
    result+=(ord(y[z])-ord(x[z]))
    z+=1
for z in range(z,len(y)):
    result+=ord(y[z])-ord('a')+1
print(result)
