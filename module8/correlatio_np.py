import numpy as np
import math


x = np.array([113,114,106,108,120,104,116,112,110,118,103,120])
y = np.array([10,15,20,15,24,11,20,20,18,24,14,27])

avg_x = sum(x)/len(x)
avg_y = sum(y)/len(y)

r_xy = sum( (x - avg_x)*(y - avg_y))/math.sqrt(sum((x - np.average(x))**2)*sum((y - np.average(y))**2))
print(r_xy)
