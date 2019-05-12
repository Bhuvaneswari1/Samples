list1=list(input())
arr = []
length = len(list1)-1
while (length>=0):
    arr.append(list1[length])
    length -= 1
if (arr == list1):
    print('YES')
else:
    print('NO')
