# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:59:22 2019

@author: SAIKAT
"""

import numpy as np
import math as m
import matplotlib.pylab as plt


x_lower=0
x_upper=10
y0=4

step_size=[0.01,0.05,0.1,0.5]

def make_graph():
    plt.figure()
        
    plt.xlabel("X-------->>>")
    plt.ylabel("Y-------->>>")
    
def f(x,y):
    return (x+20*y)*(m.sin(x*y))
def f1(x,y):
    return (-2*x**3+12*x**2-20*x+8.5)


        
def euler(xi,xf,h,initial_value):
    
    y_list=[]
    
    y=initial_value
    n=int((xf-xi)/h)
    x_list=np.arange(xi,xf+h,h)
    x_list = list(np.around(np.array(x_list),10))
    for i in range (0,n+1):
        
        
        
        y_list.append(y)
       
        tangent=f(x_list[i],y)
        y=y+tangent*h
        #x+=h
        
    return x_list,y_list

        
def SecondOrder_RK(xi,xf,h,initial_value,a2):
    y_list=[]
    y=initial_value
    n=int((xf-xi)/h)
    
    a1=1-a2
    
    p1=0.5/(a2)
  
    q11=0.5/a2
   
    x=np.arange(xi,xf+h,h)
    x= list(np.around(np.array(x),10))
    for i in range (0,n+1):
       
        
        y_list.append(y)
        #print("X:"+str(x[i])+"    Y:"+str(y_list[i]))
        k1=f(x[i],y)
        k2=f(x[i]+p1*h,y+q11*k1*h)
        y=y+(a1*k1+a2*k2)*h
        #x=x+h
    return x,y_list
    

def FourthOrder_RK(xi,xf,h,initial_value):
    y_list=[]
    y=initial_value
    n=int((xf-xi)/h)
    x=np.arange(xi,xf+h,h)
    #x= list(np.around(np.array(x),10))
    for i in range (0,n+1):
        
        y_list.append(y)
        
        k1=f(x[i],y)
       
        k2=f(x[i]+0.5*h,y+0.5*k1*h)
        
        k3=f(x[i]+0.5*h,y+0.5*k2*h)
        
        k4=f(x[i]+h,y+k3*h)
       
        y=float(y+(1/6.0)*(k1+2*k2+2*k3+k4)*h)
        #x=x+h
    return x,y_list


'''Heun Method ## a2=1/2'''
'''Midpoint Method ## a2=1'''
'''Ralston's Method ## a2=2/3'''
#FourthOrder_RK(0,4,0.5,1)
#SecondOrder_RK(0,4,0.5,1,2/3.0)



    
    
make_graph()
plt.title("Curves for Euler method for various step size")
for h in step_size:
    x_list,y_list=euler(x_lower,x_upper,h,y0)
    name=str(h)
    plt.plot(x_list,y_list,label=name)
    
    
plt.legend()
plt.show()

'''Heun Method ## a=1/2'''

make_graph()
plt.title("Curves for Heun's method for various step size")
for h in step_size:
    
    
    x_list,y_list=SecondOrder_RK(x_lower,x_upper,h,y0,0.5)
    name=str(h)
    plt.plot(x_list,y_list,label=name)
   
plt.legend()
plt.show()
    
make_graph()
plt.title("Curves for Midpoint method for various step size")
for h in step_size:
    
    x_list,y_list=SecondOrder_RK(x_lower,x_upper,h,y0,1.00)
    name=str(h)
    plt.plot(x_list,y_list,label=name)
    
plt.legend()
plt.show()

   
make_graph()
plt.title("Curves for Ralston's method for various step size")
for h in step_size:
   
    x_list,y_list=SecondOrder_RK(x_lower,x_upper,h,y0,2/3.0)
    name=str(h)
    plt.plot(x_list,y_list,label=name)
    

plt.legend()
plt.show()

    
make_graph()
plt.title("Curves for FourthOrder_RK method for various step size")
for h in step_size:
    
    x_list,y_list=FourthOrder_RK(x_lower,x_upper,h,y0)
    name=str(h)
    plt.plot(x_list,y_list,label=name)
    
    
plt.legend()
plt.show()

for h in step_size:
  
    make_graph()
    plt.title("Curves for All method for step size="+str(h))
    x_list,y_list=euler(x_lower,x_upper,h,y0)
    plt.plot(x_list,y_list,label='Euler method')
    
    
    
    
    x_list,y_list=SecondOrder_RK(x_lower,x_upper,h,y0,0.5)
    plt.plot(x_list,y_list,label='Heun method')
   
    
    x_list,y_list=SecondOrder_RK(x_lower,x_upper,h,y0,1.00)
    plt.plot(x_list,y_list,label='Midpoint method')
    
    
    x_list,y_list=SecondOrder_RK(x_lower,x_upper,h,y0,2/3.0)
    plt.plot(x_list,y_list,label='Ralston method')
   
    
    x_list,y_list=FourthOrder_RK(x_lower,x_upper,h,y0)
    plt.plot(x_list,y_list,label='Fourthorder_RK')
    
    plt.legend()
    plt.show()






        
    
        


        
        