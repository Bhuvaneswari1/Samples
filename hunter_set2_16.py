n,k=list(map(int,input().split()))
list1=[[abs(i-k),i] for i in list(map(int,input().split(" ")))]
list1.sort()
list1=list1[1:]
print(list(i[1] for i in list1[:3]))
