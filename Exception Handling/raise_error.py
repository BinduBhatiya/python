# raising using in exception handling.

a = int(input("enter the value between 1 and 10: "))

if a < 1 or a > 10:
    raise ValueError("value is not supported.")
else:
    print(a)

    