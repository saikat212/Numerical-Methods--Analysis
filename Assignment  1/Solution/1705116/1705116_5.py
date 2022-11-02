# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:50:00 2019

@author: SAIKAT
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt
x=np.linspace(0.027,0.03,50)
dic={}
def f(x):
    sp=m.sqrt((6/(2+x)))
    return ((x/(1-x))*sp)-0.05
y= [f(i) for i in x]

'''Estimation process using graphical method with code '''
for i in x:
    z=f(i)
    dic1={z:i}
    dic.update(dic1)
k=dic.keys()
p=[]

for j in k:
    if(j<0):
        j=j*(-1)
    p.append(j)

    
        
m=(min(p))
if(dic.has_key(m)):
    print(dic[m])
else:
    m=m*(-1)
    print("\n\nUsing graphical method the value of x ::\n")
    print("X= "+str(dic[m]))





plt.plot(x,y,label="f(x) VS x")

plt.xlabel("values of x----->")
plt.ylabel("values of f(x)----->")
plt.legend()
plt.grid()

plt.title("Graphical model to estimate value")
plt.savefig("2(a).pdf")

