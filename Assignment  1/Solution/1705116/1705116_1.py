# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:17:06 2019

@author: SAIKAT
"""

import numpy as np
import matplotlib.pyplot as plt
x=0.5
y=np.log(1+x)

def tylor(n):
    i=1
    p=0
    sign=1
    while(n>=1):
        p=p+((x**i)/i)*sign
        n=n-1
        sign=(-1)*sign
        i=i+1
    return p
#y1=x-(x**2)/2+(x**3)/3-(x**4)/4
#if '_name_'=='_main_':
for j in range(1,10):
    y1=tylor(j)
    print("Term="+str(j)+" and approximate value="+str(y1)+"\n")
    


