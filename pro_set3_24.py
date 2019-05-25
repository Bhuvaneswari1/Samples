n=int(input())
arr=[]
k=bin(2**n-1)[2::]
l=len(k)

for i in range(0,2**n):
   s=bin(i)[2::]
   if len(s)<l:
                        arr.append([s.count("1"),(l-len(s))*"0"+s])
   else:
                        arr.append([s.count("1"),s])
arr.sort()
for i in range(0,len(arr)):
   print(arr[i][1])
