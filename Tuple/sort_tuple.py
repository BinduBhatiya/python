# HOW TO SORT THE DATA OF TUPLE.


# METHOD 1(using sort()):
def Sort(tup):
    tup.sort(key = lambda x: float(x[1]), reverse = True)
    print(tup)

tup = [('lucky', '18.265'), ('nikhil', '14.107'), ('akash', '24.541'),  
    ('anand', '4.256'), ('gaurav', '10.365')] 
Sort(tup)

# OUTPUT :
'''
[('akash', '24.541'), ('lucky', '18.265'), ('nikhil', '14.107'), ('gaurav', '10.365'), ('anand', '4.256')]
'''


# METHOD 2(using sorted):
def Sort(tup):
    return sorted(tup, key = lambda x: float(x[1]), reverse = True)

tup = [('lucky', '18.265'), ('nikhil', '14.107'), ('akash', '24.541'),  
    ('anand', '4.256'), ('gaurav', '10.365')] 
print(Sort(tup))

# OUTPUT :
'''
[('akash', '24.541'), ('lucky', '18.265'), ('nikhil', '14.107'), ('gaurav', '10.365'), ('anand', '4.256')]
'''