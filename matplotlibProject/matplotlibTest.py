import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#解决中文输出问题
mpl.rcParams['font.sans-serif']=[u'Simhei']
mpl.rcParams['axes.unicode_minus']=False

x=np.linspace(0,10,1000)
y=np.sin(x)
z=np.cos(x**2)
plt.figure(figsize=(8,4))

plt.plot(x,y,label='$sin(x)',color='red',linewidth=2)

plt.plot(x,z,'b--',label='$cos(x^2)$')

plt.xlabel('aaa')
plt.xlabel('bbb')

plt.ylim(-1.2,1.2)

plt.legend()

plt.savefig('E:/hhh')

plt.show()

