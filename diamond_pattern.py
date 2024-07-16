'''

        *
    *   *   *
*   *   *   *   *
    *   *   *
        *

'''

for i in range(1,4):
    for k in range(4-i):
        print(' ',end=' ')
    for j in range(i*2-1):
        print('*',end=' ')
    print('\n')
for i in range(3-1,0,-1):
    for k in range(4-i,0,-1):
        print(' ',end=' ')
    for j in range(2*i-1,0,-1):
        print('*',end=' ')
    print('\n')