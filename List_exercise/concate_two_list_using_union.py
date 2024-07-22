# MERGE THE TWO LIST USING UNION.

# METHOD 1 (using "+" operator) :

def Union(lst1, lst2):
	final_list = lst1 + lst2
	return final_list

# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))                                    # [23, 15, 2, 14, 14, 16, 20, 52, 2, 48, 15, 12, 26, 32, 47, 54]


# METHOD 2 (using "sorted" function) :

def Union(lst1, lst2):
	final_list = sorted(lst1 + lst2)
	return final_list

# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))                                    # [2, 2, 12, 14, 14, 15, 15, 16, 20, 23, 26, 32, 47, 48, 52, 54]


# METHOD 3 (using "set" for not print repeat value) :

def Union(lst1, lst2):
	final_list = list(set(lst1) | set(lst2))                # if we use '+' then it throw error "TypeError: unsupported operand type(s) for +: 'set' and 'set'"
	return final_list

# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))                                    # [32, 2, 12, 14, 15, 16, 48, 47, 20, 52, 54, 23, 26]


# METHOD 4 (using simple function and '+' operator)

def conc(lst1, lst2):
	final_list = lst1 + lst2
	return final_list

# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(conc(lst1, lst2))   									# [23, 15, 2, 14, 14, 16, 20, 52, 2, 48, 15, 12, 26, 32, 47, 54]


# METHOD 5 (using simple function and '+' operator)

lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]

final_list = lst1 + lst2
print(final_list)											# [23, 15, 2, 14, 14, 16, 20, 52, 2, 48, 15, 12, 26, 32, 47, 54]
  									