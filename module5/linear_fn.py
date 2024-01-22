import matplotlib.pyplot as plt 
import numpy as np 

fig, ax = plt.subplots()

ax.spines[['left', 'bottom']].set_position(('data', 0))

ax.spines[['right', 'top']].set_visible(False)

ax.plot(1,0, '>k', transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0,1, '^k', transform=ax.get_xaxis_transform(), clip_on=False)

ax.grid(True, linestyle='-.')

x =np.linspace(-5,5,100)
# x >= 3
a = np.where(x >=3, 2*x - 1, np.nan)

# x < 3
b = np.where(x < 3, 4, np.nan)

# ax.plot(x,a, color='teal')
# ax.plot(x,b, color='red')

# plt.show()


# 2x+3y+1=0 
# ax.plot(x, -1/3 -( 2/3)*x)

# ax.plot(x, 1 / (x**2 + 2 * x + 3))
# ax.plot(x, 1 / (x**2 - 2 * x + 3))
# ax.plot(x, np.sin(x) + 2)
# ax.plot(x, np.sin(x) + -1)
# ax.plot(x,- x**2)
# ax.plot(x,np.sqrt((x + 1)))
ax.plot(x, 6 / (x - 3))






plt.show()