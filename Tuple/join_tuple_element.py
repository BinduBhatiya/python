# HOW TO JOIN THE TUPLE ELEMENT LIKE A = ('HELLO', 'PYTHON', 'WORLD') CONVERT IN ('HELLO PYTHON WORLD')

tup = ('hello', 'python', 'world')
res = ' '.join(tup)
print(res)                                  # hello python world


test_list = [('hello', 'python', 'world'), ('computer', 'science', 'portal')]
res = list(' '.join(tpl) for tpl in test_list)
print(res)                                                  # ['hello python world', 'computer science portal']

