import random
import matplotlib.pyplot as plt

upper_limit = 10

random_set = {random.randint(1, upper_limit) for _ in range(10)}
# random_set = {random.randint(1, upper_limit)}


print("Множина випадкових елементів:", random_set)


A = list(random_set)


plt.plot(A, [0] * len(A), 'ro')  # 'ro' - червоні точки
plt.title('Обмежена множина')
plt.xlabel('Елементи множини')
plt.yticks([])  # Вимкнення відображення осі y
plt.show()