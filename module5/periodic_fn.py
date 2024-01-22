import numpy as np
import matplotlib.pyplot as plt

def plot_periodic_function(func, period, title):
    x_values = np.linspace(0, 3 * period, 1000)
    y_values = func(x_values)


    plt.plot(x_values, y_values)
    plt.title(title)
    plt.legend()


plt.subplot(2, 2, 1)    #fn      #period
plot_periodic_function(np.sin, 2 * np.pi, 'Синус')


plt.subplot(2, 2, 2)
plot_periodic_function(np.cos, 2 * np.pi, 'Косинус')


plt.subplot(2, 2, 3)
plot_periodic_function(np.tan, np.pi, 'Тангенс')


plt.tight_layout()
plt.show()