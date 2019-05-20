def Reverse(list1): 
    new_lst = list1[::-1] 
    return new_lst

n=int(input())
list1=list(map(int,input().split()))
print(Reverse(list1))
