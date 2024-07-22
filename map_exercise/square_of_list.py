# PRINT THE SQUARE OF DATA IN LIST :

def sqr(x):
    return x * x
lst = [1,2,3,4,5]
res = list(map(sqr,lst))
print(res)

# OUTPUT :
# [1, 4, 9, 16, 25]
