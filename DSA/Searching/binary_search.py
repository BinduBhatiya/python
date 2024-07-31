# binary search :
# search the data is stored in which index.
# Note : 'in binary search data is must in ascending order. '

def binary_search(arr,val):
    left = 0
    right = len(arr)-1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = [1,3,5,7,9,11]
val = 9
res = binary_search(arr,val)

if res != -1:
    print(val,'found at index', res)
else:
    print('data is not found.')






