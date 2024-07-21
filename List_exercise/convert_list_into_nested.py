# CONVERT LIST INTO NESTED LIST

# METHOD 1 :

Input = ['Geeeks, Forgeeks', '65.7492, 62.5405',
         'Geeks, 123', '555.7492, 152.5406']
nes = [elem.split(', ') for elem in Input]
print(nes)

# OUTPUT :
'''
[['Geeeks', 'Forgeeks'], ['65.7492', '62.5405'], ['Geeks', '123'], ['555.7492', '152.5406']]
'''

# METHOD 2 (using 'map' and 'lambda' method) :

Input = ['Geeeks, Forgeeks', '65.7492, 62.5405',
         'Geeks, 123', '555.7492, 152.5406']
nes = list(map(lambda x:x.split(', '),Input))
print(nes)

# OUTPUT :
'''
[['Geeeks', 'Forgeeks'], ['65.7492', '62.5405'], ['Geeks', '123'], ['555.7492', '152.5406']]
'''


# METHOD 3 (using list comprehension) :

Input = ['Geeeks, Forgeeks', '65.7492, 62.5405',
         'Geeks, 123', '555.7492, 152.5406']
nes = [elem.split(', ') for elem in Input]
print(nes)

# OUTPUT :
'''
[['Geeeks', 'Forgeeks'], ['65.7492', '62.5405'], ['Geeks', '123'], ['555.7492', '152.5406']]
'''