import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

X1,Y1=np.mgrid[1:3:3j,4:5:2j]
print('X1:',X1)
print('Y1',Y1)

a=[X1.ravel(),Y1.ravel()]
print('a:',a)


grid=np.c_[X1.ravel(),Y1.ravel()]
print('X1.ravel():',X1.ravel())
print('Y1.ravel():',Y1.ravel())
print('grid:',grid)
