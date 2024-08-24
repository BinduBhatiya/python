# ACCESS ELEMENT FROM GIVEN INDEX LIST

# METHOD 1 (using list comprehension) :
itm_lst = [1,2,3,4,5,6,7]
indx_lst = [3,4]

result = [itm_lst[i] for i in indx_lst]
print("using list comprehension: ",result)                  # [4, 5]

# SUMMARY :
'''
    stp 1: for i in indx_lst (3)
    stp 2: itm_lst[i] = itm_lst[3]----> 4
    stp 3: for i in indx_lst (4)
    stp 4: itm_lst[i] = itm_lst[3]----> 5
'''



# METHOD 2 (map + __getitem__) :
itm_lst = [1,2,3,4,5,6]
indx_lst = [1,2]

result = map(itm_lst.__getitem__, indx_lst)
print("using getitem: ",list(result))                         # [2, 3]