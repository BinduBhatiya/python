# create system argument.

import sys
print(sys.argv)


# output :
# ['C:\\Users\\Bindu Bhatiya\\Desktop\\Python\\Standard module\\Sys\\sys_exercise.py']
'''
---> python sys_exercise.py 10 20 'hii' (10,20,30)
    ['sys_exercise.py', '10', '20', "'hii'", '(10,20,30)']
'''

# import first argument which is always filename

import sys
res = sys.argv
print('filename is: ',res[0])

'''
---> python sys_exercise.py
    ['sys_exercise.py']
    filename is:  sys_exercise.py
'''


# printing all element using for loop
import sys
res = sys.argv

for i in res:
    print(i)

'''
---> python sys_exercise.py 10 20 'hii' (10,20,30)
     sys_exercise.py
        10
        20
        'hii'
        (10,20,30)
'''


# program to check whether character is present or not.

import sys
res = sys.argv

if res[1] in res[2]:
    print('found')
else:
    print('not found')

'''
---> python sys_exercise.py y python
    found
---> python sys_exercise.py a python
    not found
'''