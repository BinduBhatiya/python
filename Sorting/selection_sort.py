def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [40,30,10,50,20]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)


# [10,20,30,40,50]
