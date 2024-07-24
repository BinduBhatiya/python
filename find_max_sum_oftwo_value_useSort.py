# find max two value sum in list

# lst = [2,5,15,10,3,12]
# res = sorted(lst)
# print('list value is: ',res)
# len = len(res)
# sum = res[len-1] + res[len-2]
# print('maximum value is: ',res[len-1],',',res[len-2])
# print('max value sum is : ',sum)


# METHOD 2 :

def list_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                

#lst = [2,5,15,10,3,12]
lst = [7,2,11,6,8,20,9]
list_sort(lst)
n = len(lst)
print('sum of two maximum value is:',lst[n-1],lst[n-2])
#print('sorted list is: ',lst)




