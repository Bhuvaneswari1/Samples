n=input()
str1=''
c,i=0,0
while i<len(n)-1:
  if n[i]=='a' and n[i+1]=='b':
    str1+=n[i]+n[i+1]
    i+=2
  else:
    str1=''
    i+=1
if c<len(str1):
    c=len(str1)
x=len(n)-1
if n[x]=='a' and n[x-1]=='b' and str1!='':
  c+=1
print(c)
