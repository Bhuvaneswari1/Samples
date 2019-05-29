arr=input()
s=''
for i in range(0,len(arr)-1,2):
        try:
            if (arr[i+1]+(arr[i+2]))=='10':
                s+=arr[i]*10
            else:
                if int(arr[i+1])%2==0:
                    s+=arr[i]*int(arr[i+1])
                else:
                    s+=arr[i]+arr[i+1]
        except:
                if int(arr[i+1])%2==0:
                    s+=arr[i]*int(arr[i+1])
                else:
                    s+=arr[i]+arr[i+1]
print(s)
