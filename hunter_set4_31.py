def maxprodsubarray(a):
    curr_max_product = a[0]
    prev_max_product = a[0]
    prev_min_product = a[0]
    ans=a[0]
    for i in range(1,len(a)):
        curr_max_product = max(prev_max_product*a[i],prev_max_product*a[i],a[i])
        curr_min_product = min(prev_min_product*a[i],prev_min_product*a[i],a[i])
        ans=max(ans,curr_max_product)
        prev_max_product=curr_max_product
        prev_min_product=curr_min_product
    return ans

n=int(input())
l=list(map(int,input().split()))
arr=[]
for i in range(0,n):
    arr.append(l[i])
print(maxprodsubarray(arr))
