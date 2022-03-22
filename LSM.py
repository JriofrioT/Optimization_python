# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np

Phi=np.array([[0,1],[1,1],[2,1],[3,1],[4,1],[5,1]])
Y=np.array([[15],[10],[9],[6],[2],[0]])

Theta_ls=np.linalg.lstsq(Phi,Y,rcond=None)[0]
print (Theta_ls)

print("hello world")

#Verification

theta_ls=np.linalg.inv(Phi.transpose()*np.mat(Phi)) * Phi.transpose() * Y
print(theta_ls)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
