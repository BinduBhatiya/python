names = ['apple','google','yahoo','gmail',['java','c#','python','ruby'],'walmart']

print(names[3])           # gmail

print(names[-1])           # walmart

print(names[4][1])         # c#

print(names[4])            # ['java','c#','python','ruby']

print(names[4][2][::2])     # 'pto'

print(names[-1][-4::])     # 'mart'

print(names[-1][3::])      # 'mart'

print(names[2][2::])       # 'hoo'

print(names[2][-3::])      # 'hoo'

bikes = ['hayabusa','himalayan','royal enfield','rx100','splendor','ryder','fz','hero delux',
         ['luna50','access','avtiva5g','jupiter','maestro','scotty-pep',['ola','ather','revolt'],
          'navi','apacherr310'],'harley','beneli','kawasaki','ducati','bmw']

print(bikes[7][-4:-1:])        # 'elu'

print(bikes[7][7:10:])         # 'lux'

print(bikes[-2][2:-2])         # 'ca'

print(bikes[-2][2:-1])         # 'cat'

print(bikes[-2][2:6])          # 'cati'

print(bikes[-2][2:5])          # 'cat'

print(bikes[-6][-1][2:6])      # 'ache'

print(bikes[8][6][0])          # 'ola'

print(bikes[8])                # 'luna50','access','avtiva5g','jupiter','maestro','scotty-pep','ola','ather','revolt'

print(bikes[8][6])             # 'ola','ather','revolt'

print(bikes[6])                # 'fz'

print(bikes[-2])               # 'ducati'

print(bikes[12])               # 'ducati'

print(bikes[8][0])             # 'luna50'

print(bikes[-2])               # 'ducati'

print(bikes[12])               # 'ducati'

print(bikes[8][7])             # 'navi'

print(bikes[8][-2])            # 'navi'

print(bikes[-6][-2])           # 'navi'