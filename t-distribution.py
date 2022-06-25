# 不同自由度的学生t分布与标准正态分布
import numpy as np
from scipy.stats import norm
from scipy.stats import t
import matplotlib.pyplot as plt

print('比较t-分布与标准正态分布')
x = np.linspace( -3, 3, 100)
plt.plot(x, t.pdf(x,1), label='df=1')
plt.plot(x, t.pdf(x,2), label='df=20')
plt.plot(x, t.pdf(x,100), label = 'df=100')
plt.plot( x[::5], norm.pdf(x[::5]),'kx', label='normal')
plt.legend()
plt.show()
