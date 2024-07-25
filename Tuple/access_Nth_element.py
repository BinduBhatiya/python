# HOW TO ACCESS Nth ELEMENT FROM TUPLE.

# METHOD 1(using list comprehension):
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

res = [lis[1] for lis in test_list]
print('access the element: ',res)

# OUTPUT :
'''
access the element:  ['Rash', 'Varsha', 'Kil']
'''

# METHOD 2(using zip):
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

n = 1
res = list(map(lambda x: x[n], test_list))
print("List with only nth tuple element:", res)

# OUTPUT :
'''
List with only nth tuple element:  ['Rash', 'Varsha', 'Kil']
'''