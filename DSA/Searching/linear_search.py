# linear search :
# find the value is store in which index.

def linear(arr,val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1
arr = [1,2,3,4,5,6]
val = 3        
res = linear(arr,val)

if res != -1:
    print('date',val,'found at index',res)
else:
    print('data is not found.')


# output :
# date 3 found at index 2
