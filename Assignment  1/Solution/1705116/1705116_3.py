# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:56:00 2019

@author: SAIKAT
"""

import numpy as np
#import code1 as cd
import matplotlib.pyplot as plt
x=np.arange(-0.9,1.1,0.1,dtype=float)


y1=np.log(1+x)


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
    
    
y2=tylor(1)
y3=tylor(3)
y4=tylor(5)
y5=tylor(20)
y6=tylor(50)


plt.plot(x,y1,label="Exact figure of ln(1+x)",color='red')
plt.plot(x,y2,label="T-1",color='blue')
plt.plot(x,y3,label="T-3",color='black')
plt.plot(x,y4,label="T-5",color='orange')
plt.plot(x,y5,label="T-20",color='green')
plt.plot(x,y6,label="T-50",color='violet')
plt.xlabel("values of x")
plt.ylabel("values of ln(1+x)")
plt.title("-< Graph for 1(c) ->")
plt.legend()
plt.grid()
plt.savefig("Graph_for_1(c)_not.pdf")



