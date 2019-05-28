n,m=map(int,input().split())
arr=[]
count=0
for i in range(n):
    arr.append(input())
for i in range(n):
    for j in range(m-1):
        if arr[i][j]=="R" and arr[i][j+1]=="R":
            count+=5
        elif arr[i][j]=="G" and arr[i][j+1]=="G":
            count+=3
print(count)
