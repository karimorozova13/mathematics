import matplotlib.pyplot as plt
from sympy import *
import numpy as np

x= Symbol('x')
y = x**6 + 2* x**5 - 30* x**4 + 16* x**3 - 12* x**2 + x + 3

# diff
yprime = y.diff(x)


# f'(x)
y1 = 6*x**5 + 10*x**4 - 120*x**3 + 48*x**2 -24*x + 1


# graph
fig, ax = plt.subplots()

ax.spines[["left", "bottom"]].set_position(("data", 0))

ax.spines[["top", "right"]].set_visible(False)

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.grid(True, linestyle='-.')

x = np.linspace(-1, 4, 100, False)

# Функціональну залежність
ax.plot(x, 6*x**5 + 10*x**4 - 120*x**3 + 48*x**2 -24*x + 1)

plt.show()

for i in range(6000):
    x = -1+ i/1000
    y = 6*x**5 + 10*x**4 - 120*x**3 + 48*x**2 - 24*x + 1
    if abs(y)<0.01:
        print(y,x)


for i in range(6000):
    x = 2+ i/1000
    y = 6*x**5 + 10*x**4 - 120*x**3 + 48*x**2 - 24*x + 1
    if abs(y)<1:
        print(y,x)
        
x= 0.04499999999999993
y =x**6+2*x**5-30*x**4+16*x**3-12*x**2+x+3
print(f"y1={y}")


x= 3.4939999999999998
y =x**6+2*x**5-30*x**4+16*x**3-12*x**2+x+3
print(f"y2={y}")