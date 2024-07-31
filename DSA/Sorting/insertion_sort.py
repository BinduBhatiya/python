# sorting the data using insertion sort.

def insertion(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i-1
        # for j in range(0,n-1):
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
lst = [40,20,30,10,50]
insertion(lst)
print(lst)                                      # [10, 20, 30, 40, 50]

