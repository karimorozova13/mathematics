import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz
from matplotlib.patches import Polygon

X=np.linspace(0,7)
Y=((X - 3) * (X - 5) * (X - 7) + 85) # функція
plt.plot(X,Y,'k-',label='Функція')

Y1=np.diff(Y)/np.diff(X) # похідна
plt.plot(X[:-1],Y1,'k--',label='Похідна')
Y1=np.gradient(Y,X[1]-X[0]) # або
plt.plot(X,Y1,'k--')

Y_int=cumtrapz(Y, X, initial=0) # первісна
plt.plot(X,Y_int,'k:',label='Первісна')
plt.xlabel('$x$')
plt.ylabel('$y$')
legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
plt.grid()
plt.show()

# Задаємо функцію
def func(x):
    return x**3 - 15* x**2 + 71*x - 20
    # return (x - 3) * (x - 5) * (x - 7) + 85



# Границі інтегрування
a, b = 2, 9  # integral limits
# Діапазон зміни x
x = np.linspace(0, 10)
# Розраховуємо значення y
y = func(x)


fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)


# Оформлюємо область
# Генеруємо значення x та y в області інтегрування
ix = np.linspace(a, b)
iy = func(ix)


# Зафарбовуємо область
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)


# Розміщуємо текст інтеграла всередині області
ax.text(0.5 * (a + b), 30, r"$\int_2^9 f(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)


# Підписуємо осі
fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')


# Ховаємо верхню та праву границі
ax.spines[['top', 'right']].set_visible(False)


# Змінюємо підписи на осях
ax.set_xticks([a, b], labels=['$xa=2$', '$xb=9$'])
ax.set_yticks([])


plt.show()