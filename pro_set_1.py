n=int(input())
m=[]

for i in range(0,n):
    arr=input()
    m.append(arr)
lng_common_prefix=[]

for i in zip(*m):
    if i.count(i[0])==len(i):
        lng_common_prefix.append(i[0])
    else:
        break
result=''.join(lng_common_prefix)
print(result)
