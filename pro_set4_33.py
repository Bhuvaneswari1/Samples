str1=input()
for i in range(len(str1)):
  arr=str1[i::]
  #print("arr[0]=",arr[0])
  #print("str1[0]=",str1[0])
  if arr[0]>str1[0]:
    print(arr)
    break
