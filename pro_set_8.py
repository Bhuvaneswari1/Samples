from math import gcd
from functools import reduce

n,q = map(int,input().split())

in_nums = list(map(int, input().split()))

for i in range(q):
    l, r = map(int, input().split())
    if(i==1):
        g = reduce(gcd, in_nums[l-1:r])
    else:
        g1=reduce(gcd, in_nums[l-1:r])
print(g)
print(g1)
