import numpy as np 
import matplotlib.pyplot as plt

# css for label and title value.
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)

plt.title('sport watch data', loc='left',fontdict = font1)   # it can show the title of the graph. 'loc' is Legal values are: 'left', 'right', and 'center'. Default value is 'center'.
plt.xlabel('x label',fontsize=12,fontdict = font2)       # it can show the x label name
plt.ylabel('y label',fontsize=12,fontdict = font2)       # it can show the y label name

# You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.

plt.show()

