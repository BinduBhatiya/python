# REMOVE EMPTY TUPLE FROM TUPLE LIST.


tuples = [(), ('hello','python'), (), ('python','world')]
res = []
for i in range(len(tuples)):
    if tuples[i] != ():
        res.append(tuples[i])
print(res)


# OUTPUT :
# [('hello','python'),('python','world')]

