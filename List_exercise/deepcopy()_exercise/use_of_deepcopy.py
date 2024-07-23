# USE OF DEEPCOPY IN PYTHON.

# EXERCISE 1:
import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
b[2].append(5)
print(a)  # Output: [1, 2, [3, 4]]
print(b)  # Output: [1, 2, [3, 4, 5]]


                                                # deepcopy()  VS  copy()

# EXERCISE 2:
import copy

a = [1, 2, [3, 4]]
b = copy.copy(a)
b[3].append(5)
print(a)  # Output: [1, 2, [3, 4, 5]]
print(b)  # Output: [1, 2, [3, 4, 5]]


