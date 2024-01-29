import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats


N=1000
X = [] 


# Цикл з 1000 ітерацій, на кожній з яких додаємо 1 випадковий елемент з нормальним розподілом, із середнім 10 та стандартним відхиленням 5
for i in range(N):
    X.append(random.normalvariate(10,3))


mean,std = stats.norm.fit(X)



k2,pvalue = stats.normaltest(X) # тест на нормальний розподіл (k2 - сума квадратів коефіцієнтів асиметрії і ексцесу)
print (f"Перевірка на відповідність нормальному розподілу: {k2},pvalue = {pvalue}>0.05") # наприклад, якщо pvalue < 0.05, то це не нормальний розподіл


# формується 2 масиви: n - кількість елементів, що потрапили в інтервал, x - масив границь інтервалів
n,x=np.histogram(X, bins=10)


xmin=x[:-1]


dx=x[1]-x[0]


y=n/N


# масив центрів інтервалів
xmid=xmin+dx/2
# виводимо емпіричну гістограму приведених частот
plt.bar(xmid, y, width=dx, color='y')


el_min = min(X)
el_max = max(X)
X1=np.linspace(el_min,el_max,1000) # аргументи для побудови теоретичної кривої
dist2 = stats.norm(loc=mean, scale=std) # нормальний розподіл із параметрами після підгонки
plt.plot(X1, dist2.pdf(X1),'k-') # нарисувати теоретичну криву густини ймовірності


plt.xlabel('x')
plt.ylabel('Частота (ймовірність)')


plt.grid()
plt.show()