# CREATE A LIST OF TUPLE USING LIST AND TUPLE

# CREATE
tpl = [(1,'hello'), (2,'how'), (3,'are'), (4,'you')]
print(tpl)

# OUTPUT :
# [(1, 'hello'), (2, 'how'), (3, 'are'), (4, 'you')]


# CREATE LIST OF TUPLE USING "ZIP()" FUNCTION.
tp1 = (1,2,3,4,5)
tp2 = ('hello', 'python', 'world', 'how', 'R you?')

res = zip(tp1,tp2)
print(list(res))

# OUTPUT :
# [(1, 'hello'), (2, 'python'), (3, 'world'), (4, 'how'), (5, 'R you?')]


# CREATE LIST OF TUPLE USING "iter()" FUNCTION.

tp1 = ('hello', 'python', 'world', 'how', 'R you?')

res = [x for x in zip(*iter(tp1))]
print(res)

# OUTPUT :
# [('hello',), ('python',), ('world',), ('how',), ('R you?',)]


# CREATE LIST OF TUPLE USING "map()" FUNCTION.
tp1 = [['hello'], ['python'], ['world']]

res = list(map(tuple,tp1))
print((res))

# OUTPUT :
# [('hello',), ('python',), ('world',)]