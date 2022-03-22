# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# *******SIMPLE SOLUTION*******
#---------variables-----------------
xstart = -20
xstop = 20
delta = 0.1
#---------function------------------
x = np.arange(xstart,xstop,delta)
aux_1 = x*x
y = 2*aux_1 + 20*x - 22
#----------plot---------------------


i=0

while y[i] > y[i+1]:
    i=i+1

print(x[i])
print(y[i])

# *******SCALAR FUNCTION (SciPy)*******
# ----- Definition of function---------
def func(x_1):
    y_1 = 2*x_1**2 + 20*x_1 -22
    return y_1
xmin=-20
xmax=20
dx=0.1
N=int((xmax-xmin)/dx)
x_1=np.linspace(xmin,xmax,N+1)
y_1=func(x_1)
#-----------Plot------------------------

plt.plot(x_1,y_1)
plt.xlim([xmin,xmax])
plt.grid()
plt.show()

x_min = optimize.fminbound(func,xmin,xmax)
y_min = func(x_min)

print(x_min)
print(y_min)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
