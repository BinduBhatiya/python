import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker='o')     # circle

# plt.plot(ypoints, marker='o', ms=20)      # ms = marker size 

# plt.plot(ypoints, marker='o', ms=20, mec='r') # mec = marker edge color

plt.plot(ypoints, marker='o', ms=20, mfc='r') # mec = marker face color

# plt.plot(ypoints, 'o:r')        
''' dotted  "here, o:r in which 'r' it means "RED color" of line,
    but it not support all character of color.it support only 
    red, blue, cyan, yellow, black, white, magenta, green Thats it. 
    here, only for black color use 'k' character for any other color use only first character.'''

# plt.plot(ypoints, 'o--')      # doubledashed line

# plt.plot(ypoints, 'o-.')      # dashed_dotted line

plt.show()