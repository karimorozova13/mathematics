import matplotlib.pyplot as plt
from sympy import diff, symbols

fig, ax = plt.subplots()

ax.spines[['left', 'bottom']].set_position(('data', 0))

ax.spines[['right', 'top']].set_visible(False)

ax.plot(1,0, '>k', transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(1,0, '^k', transform=ax.get_xaxis_transform(), clip_on=False)

ax.grid(True, linestyle='-.')

x,y = symbols('x y')

# fx =x**2 - 3*x +5 
# fx =x**3 - 4 
# fx =x**4 + 5* x**3 - 10*x
fx =x**5 - 4* x**4 + x**2 + 10*x



# derivative, differentiation (похідна) 
dx = diff(fx)

k=[]
n=[]
l=[]

for i in range(1000):
    j = (i-300)*0.01
    k.append(j)
    n.append(dx.subs(x,j))
    l.append(fx.subs(x,j))
    

ax.plot(k,n)
ax.plot(k,l)

plt.show()
