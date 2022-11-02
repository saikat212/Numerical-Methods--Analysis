# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:17:06 2019

@author: SAIKAT
"""

import numpy as np
import matplotlib.pyplot as plt
x=0.5
AValue=[]
t=np.log(1+0.5)


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
    
def Eror_calculation(x):
    er=np.abs(((t-x)/t)*100)
    return er
#y1=x-(x**2)/2+(x**3)/3-(x**4)/4
#if '_name_'=='_main_':
for j in range(1,51):
    y1=tylor(j)
    AValue.append(y1)

AEror=[Eror_calculation(j) for j in AValue]
term=np.arange(1,51,1)
print(AEror)
plt.title("Graph for 1(d)")
plt.plot(term,AEror,label="Relative Approx. Eror VS Number of terms",color='red')
plt.xlabel("Number of Terms------>",fontsize=20)
plt.ylabel("Relative Approximation Eror--->",fontsize=15)
plt.grid()
plt.legend()
plt.savefig("Graph for 1(d).pdf")

        


