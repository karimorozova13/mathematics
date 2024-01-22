import matplotlib.pyplot as plt 
import numpy as np 

fig, ax = plt.subplots()

ax.spines[['left', 'bottom']].set_position(('data', 0))

ax.spines[['right', 'top']].set_visible(False)

ax.plot(1,0, '>k', transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0,1, '^k', transform=ax.get_xaxis_transform(), clip_on=False)

x = np.linspace(-10,10,100)

ax.grid(True, linestyle='-.')

# y = x**2 + 2
ax.plot(x, x**3 + 3)
plt.show()
