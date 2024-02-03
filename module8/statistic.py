import numpy as np
import statistics as st
import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

x1=[6,7,4,5,4,5,3,6,7,3,7,3,5,4,4,3,5,4]
x2=[4,4,5,4,1,5,5,3,3,6,2,3,4,3,7,5,3,2,4,5]


x1_avg = np.average(x1)
x2_avg = np.average(x2)


x1_disp = st.variance(x1)
x2_disp = st.variance(x2)


n1 = len(x1)
n2 = len(x2)



print(f"Середні значення: {x1_avg} {x2_avg}" )
print(f"Дисперсії: {x1_disp} {x2_disp}" )
print(f"Розмір вибірки: {n1} {n2}" )


t = (x1_avg-x2_avg)/(math.sqrt((((n1-1)*x1_disp+(n2-1)*x2_disp))/(n1+n2-2)*(1/n1+1/n2)))
print(t)


file_path = 'mat_stat.csv'
# Створи об'єкт, який міститиме в собі наш датасет
value_data = pd.read_csv(file_path, sep = ';')

value_data.describe()
# value_data.head()

N=len(value_data.Q106) # розмір вибірки
X = value_data.Q106

mean,std = stats.norm.fit(X)


# формується 2 масиви: n - кількість елементів, що попали в інтервал, x - масив меж інтервалів
print(np.histogram(X, bins=13))
n,x=np.histogram(X, bins=13)

# масив початків інтервалів (прибрали останнє, найбільше значення)
xmin=x[:-1]

# ширина інтервалу (різниця двох послідовних стовпчиків).
dx=x[1]-x[0]

# емпірична приведена частота: частка від кількості елементів в інтервалі та загальної кількості елементів.
y=n/N

# масив центрів інтервалів
xmid=xmin+dx/2
# виводимо емпіричну гістограму приведених частот
plt.bar(xmid, y, width=dx, color='y')

X1=np.linspace(-2,10,1000)
dist2 = stats.norm(loc=mean, scale=std)
plt.plot(X1, dist2.pdf(X1),'k-')


plt.xlabel('x')
plt.ylabel('Частота (ймовірність)')

plt.grid()
plt.show()


