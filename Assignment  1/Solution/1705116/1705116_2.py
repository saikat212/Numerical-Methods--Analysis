# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:56:00 2019

@author: SAIKAT
"""

import numpy as np

import matplotlib.pyplot as plt
x=np.arange(-0.9,1.1,0.1,dtype=float)
y=np.log(1+x)
plt.plot(x,y,label="Exact figure of ln(1+x)",color='red',linewidth=2)
plt.xlabel("values of x")
plt.ylabel("values of ln(1+x)")
plt.legend()
plt.grid()
plt.title("Plot for 1(B)")
plt.savefig("1(b).pdf")
