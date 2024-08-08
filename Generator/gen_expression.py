x = (x*5 for x in range(5) if x%2==0)

print(x)        # <generator object <genexpr> at 0x000001989A1442B0>
print(next(x))  # 0
print(next(x))  # 10
print(next(x))  # 20