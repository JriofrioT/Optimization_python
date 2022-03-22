# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import scipy.optimize as opt

def banana(var):
    a=1
    b=100
    x, y = var
    f= (a-x)**2 + b*(y-x**2)**2
    return f
xopt = opt.minimize(banana,x0=[-1.2,1])
#xopt = opt.fmin(func=banana,x0=[-1.2,1])

print(xopt)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
