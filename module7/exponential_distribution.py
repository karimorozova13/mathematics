import numpy as np
import matplotlib.pyplot as plt
import random



N=1000 
X = [] 


# Цикл з 1000 ітерацій, на кожній з яких додаємо 1 випадковий елемент з нормальним розподілом, із середнім 10 та стандартним відхиленням 5
for i in range(N):
    X.append(random.expovariate(1/20))


print(np.histogram(X, bins=10))
n,x=np.histogram(X, bins=10)


xmin=x[:-1]


dx=x[1]-x[0]


y=n/N


# масив центрів інтервалів
xmid=xmin+dx/2
# виводимо емпіричну гістограму приведених частот
plt.bar(xmid, y, width=dx, color='y')


plt.xlabel('x')
plt.ylabel('Частота (ймовірність)')


plt.grid()
plt.show()