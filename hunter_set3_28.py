s=list(input())
dup_chr=""
arr=[]
for i in range(0,len(s)):
    if s[i] not in arr:
        arr.append(s[i])
print(dup_chr.join(arr))
