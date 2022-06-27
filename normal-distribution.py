#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:25:19 2022

@author: wuqf
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import math

# normal distribution
# z distribution if u is 0 and sig is 1
u = 0
sig = math.sqrt(4)

x = np.linspace(u - 5 * sig, u + 5 * sig, 2000)
y1 = stats.norm.pdf(x, u, sig)

plt.rc('font', family='Arial Unicode MS', size=14)
plt.plot(x, y1, label='N({},{})'.format(u, sig))
plt.title("z-distribution")
plt.legend()
plt.grid(True)
plt.show()
