import matplotlib.pyplot as plt 
import numpy as np 

# even fn
# f(x) = f(-x)

# odd fn
# f(x) = -f(x)


# EVEN FN
def quadratic_function(x):
    return x**2

def cosine_function(x):
    return np.cos(x)

def absolute_value_function(x):
    return np.abs(x)


x_values = np.linspace(-5, 5, 100)


plt.figure(figsize=(12, 4))


plt.subplot(1, 3, 1)
plt.plot(x_values, quadratic_function(x_values), label=r'$f(x) = x^2$')
plt.plot(x_values, quadratic_function(-x_values), linestyle='--', label=r'$f(-x) = x^2$')
plt.title('Квадратична функція')
plt.legend()


plt.subplot(1, 3, 2)
plt.plot(x_values, cosine_function(x_values), label=r'$f(x) = \cos(x)$')
plt.plot(x_values, cosine_function(-x_values), linestyle='--', label=r'$f(-x) = \cos(x)$')
plt.title('Косинус')
plt.legend()


plt.subplot(1, 3, 3)
plt.plot(x_values, absolute_value_function(x_values), label=r'$f(x) = |x|$')
plt.plot(x_values, absolute_value_function(-x_values), linestyle='--', label=r'$f(-x) = |x|$')
plt.title('Модуль x')
plt.legend()


plt.tight_layout()
plt.show()