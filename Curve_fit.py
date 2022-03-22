# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


start = 0
stop =2*np.pi
delta = 0.5
x = np.arange(start,stop,delta)

a = 2
b = 10
np.random.seed()
y_noise = 0.2*np.random.normal(size=x.size)
y = a * np.sin(x+b)
y = y + y_noise

#plt.subplot(2,1,1)
plt.plot(x,y,'or')

def model (x, a, b):
    y = a * np.sin(x+b)
    return y
popt,pcov = curve_fit(model,x,y)
print(popt)

delta_1= 0.1
xmodeldata=np.arange(start,stop,delta_1)

ymodel=model(xmodeldata,*popt)

#plt.subplot(2,1,2)
plt.plot(xmodeldata,ymodel)
plt.grid()
plt.show()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
