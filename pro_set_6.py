Given_number=int(input())
m=input().split()
n=[]
num_triplet=0
for i,j in enumerate(m):
   n.insert(i,j)
for i in range(0,len(n)-2):
   for j in range(1,len(n)-1):
      for k in range(2,len(n)):
         if(n[i]<n[j]<n[k])and(i<j<k):
            num_triplet=num_triplet+1
print(num_triplet)
