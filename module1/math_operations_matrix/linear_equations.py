import numpy as np 

# Solving a system of linear equations

# AX = B

# TASK 1
A= np.array([[3,0,0],
             [2,1,0],
             [1,1,1]])
B = np.array([60,50,90])
X = np.linalg.solve(A,B)
print(X)
# X  = np.array([x,y,z])


a= np.array([[2,3,2],[1,2,-3],[3,4,1]])
det_a = np.linalg.det(a)
inv_a = np.linalg.inv(a)

# TASK 2
c= np.array([[3,0,0],
             [1,2,0],
             [0,1,-1]])
d = np.array([30,18,2])
z= np.linalg.solve(c,d)
res = z[2] + z[1] * z[0]
print(z)
print(res)

# TASK 3
e = np.array([[2,3,4],
             [1,2,0],
             [3,0,1]])
k = np.array([150,70,90])
r = np.linalg.solve(e,k)
print(r)

# TASK 4
q = np.array([[1,0,0,4,2],
              [0,1,1,0,1],
              [0,1,1,3,0],
              [1,0,1,0,1],
              [0,0,5,5,5]])
w = np.array([220,180,200,160,600])
t = np.linalg.solve(q,w)
print(t)






