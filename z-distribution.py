#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:25:19 2022

@author: wuqf
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#z distribution

x=np.linspace(-5,5,2000)
y1=stats.norm.pdf(x,0,1)
plt.rc('font',family='Arial Unicode MS',size=14)
plt.plot(x,y1,label='N(0,1)')
plt.title("z-distribution")
plt.legend()
plt.show()
