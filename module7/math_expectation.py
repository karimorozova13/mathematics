import matplotlib.pyplot as plt
import numpy as np

# discrete
# M(X)= sum(Xi*Pi)

n = [0.0016,0.0256,0.1536,0.4096,0.4096]


# plot
fig, ax = plt.subplots()


ax.plot(n, linewidth=3.0)


ax.set(xlim=(0, 4), xticks=np.arange(0, 4.1),
       ylim=(0, 0.5), yticks=np.arange(0, 0.5,0.1))
plt.grid(True)
plt.show()


# графік функції розподілу 
n1 = [0.0016,0.0272,0.1808,0.5904,1]
print(n1)
plt.stairs(n1, fill=True, label='Distribution')
plt.grid(True)
plt.show()