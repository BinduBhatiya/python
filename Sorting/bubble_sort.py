# BUBBLE SORT

lst = [20,10,40,30,5]
n = len(lst)
for i in range(n):
    for j in range(n-i-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
print('after sorting : ',lst)