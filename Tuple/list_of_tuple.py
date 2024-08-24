# CREATE A LIST OF TUPLE USING LIST AND TUPLE

# method 1:
# CREATE
tpl = [(1,'hello'), (2,'how'), (3,'are'), (4,'you')]
tp1,tp2 = zip(*tpl)
print("method 1 : ")
print(tp1)
print(tp2)

# OUTPUT :
# [(1, 'hello'), (2, 'how'), (3, 'are'), (4, 'you')]


# method 2:
# CREATE LIST OF TUPLE USING "ZIP()" FUNCTION.
tp1 = (1,2,3,4,5)
tp2 = ('hello', 'python', 'world', 'how', 'R you?')

res = zip(tp1,tp2)
print("method 2 using zip: ",list(res))

# OUTPUT :
# [(1, 'hello'), (2, 'python'), (3, 'world'), (4, 'how'), (5, 'R you?')]


# method 3:
# CREATE LIST OF TUPLE USING "map()" FUNCTION.
tp1 = [['hello'], ['python'], ['world']]

res = list(map(tuple,tp1))
print("method 3: ",res)

# OUTPUT :
# [('hello',), ('python',), ('world',)]