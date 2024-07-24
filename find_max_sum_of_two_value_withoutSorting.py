def list_max(lst):  
    l = 0
    m = []
    n = len(lst)
    a = len(m)

    for j in range(n):
        if j+1 < n: 
            sum = lst[j] + lst[j+1]
        if l < sum:
            l = sum
            max1 = lst[j]
            max2 = lst[j+1]
        else:
            m.append(max1)
            m.append(max2)
            continue
                
    print('max value is: ',m[a-2],m[a-1])             
                                          
#lst = [2,5,15,10,3,12]
lst = [7,2,11,6,8,20,9]
list_max(lst)




    