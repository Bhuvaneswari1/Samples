def reduce(N,K):
   if K<=0:
     return N
   if N==0:
     return 10
   a=reduce(N//10,K)*10+N%10
   a1=reduce(N//10,K-1)
   #print("a=",a)
   #print("a1=",a1)
   if a<a1:
     return a
   else: 
     return a1
N,K=map(int,input().split())
print(reduce(N,K))
