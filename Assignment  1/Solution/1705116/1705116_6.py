
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 22:11:02 2019

@author: SAIKAT
"""
import math as m
import numpy as np

def f(x):
    sp=m.sqrt((6/(2+x)))
    return ((x/(1-x))*sp)-0.05

#f=lambda x: ((x/(1-x))*m.sqrt((6.0/(2+x))))-0.05
    
    
def False_f(xl,xu):
    return (xu-((f(xu)*(xl-xu))/(f(xl)-f(xu))))
    
    
def Secant_f(x0,x1):
    return (x1-(((x1-x0)/(f(x1)-f(x0)))*f(x1)))
    
def False_position_method(f,xl,xu,es,m):
    F_IN=0
    i=0
    try:
        if(f(xl)*f(xu)<0):
           
            xr0=0
            ea=1.1*es
            while(ea>=es and i<m):
                F_IN+=1
                i+=1
                xr=False_f(xl,xu)
                if(xr!=0 and i!=1):
                    ea=(np.abs((xr-xr0)/xr))*100
                test=f(xl)*f(xr)
                if(test==0):
                    ea=0
                elif(test<0):
                    xu=xr
                    xr0=xr
                else:
                    xl=xr
                    xr0=xr
            
            print("\n\nError for false_position:: "+str(ea)+"\n") 
            if(i<=m and ea<=es):
                return xr,F_IN
            else:
                 return "Not found.Need more iteration.\n",F_IN
                
               
        return "Incorrect Guess . change and try.",F_IN
    except ZeroDivisionError:
        return "To determine f(x) has an error about ZeroDivisionError",F_IN
   
   
    
             
            
               
                
def Secant_method(f,x0,x1,e,m):
    S_IN=0
    try:
        if(f(x0)*f(x1)<0):
           
            for i in range(1,m+1):
                S_IN+=1
                xn=Secant_f(x0,x1)
                er=((np.abs(xn-x1)/xn)*100)
                if(er<=e):
                    print("Error for secant method:: "+str(er)+"\n")
                    return xn,S_IN
                else:
                    x0=x1
                    x1=xn
            
            return "Not Found.Need More Iteration.",S_IN
        return "Incorrect Guess . change and try",S_IN
    except ZeroDivisionError:
        return "To determine f(x) has occured ZeroDivisionError:",S_IN
        
        
    
    
    
            
                
r1=list(False_position_method(f,0.01,0.5,0.5,20))

r2=list(Secant_method(f,0.01,0.5,0.5,20))


print("Result of False position Method:\n")
print("       Value of x= "+str(r1[0])+"\n")
print("       Numbers of iteration= "+str(r1[1])+"\n\n\n")

print("Result of Secant Method:\n")
print("       Value of x= "+str(r2[0])+"\n")
print("       Numbers of iteration= "+str(r2[1])+"\n")
               

