# find the square of odd number.

# METHOD : 1

odd_square = []

for i in range(1,10):
    if i % 2 == 1:
        odd_square.append(i**2)
print(odd_square)

# METHOD : 2

odd_square = [x**2 for x in range(1,10) if x % 2 == 1]
print(odd_square)
