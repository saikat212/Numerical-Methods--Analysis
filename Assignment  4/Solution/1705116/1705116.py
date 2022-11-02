# -*- coding: utf-8 -*-
"""
Created on Mon Aug 05 17:06:56 2019

@author: SAIKAT
"""

import numpy as np
import matplotlib.pylab as plt

x=[]
f=[]
my_file=open("input.txt","r")
list_lines=my_file.readlines()
N=int(list_lines[0])
for i in range(1,N+1):
    s=list_lines[i]
    s1=s.split(" ")
    x.append(float(s1[0]))
    f.append(float(s1[1]))




plt.grid()
plt.xlabel("X--------->")
plt.ylabel("f(X)--------->")
plt.plot(x,f,color='red',label="simpson 1/3")
plt.plot(x,f,color='yellow',label="simpson 3/8")
plt.plot(x,f,color='green',label="Trapezoidal rule")

plt.legend()

plt.scatter(x,f)

plt.show()




#################################


def Trap(h,f0,f1):
    return h*((f0+f1)/2)

def sim13(h,f0,f1,f2):
    return (h/3)*(f0+4*f1+f2)
    
def sim38(h,f0,f1,f2,f3):
    return ((3*h)/8)*(f0+3*(f1+f2)+f3)

def unequally_space(n,x,f):
    h=x[1]-x[0]
    k=1
    t=0
    s1=0
    s3=0
    sum=0
    for j in range(1,n):
        if(j<n-1):
            
            
            hf=x[j+1]-x[j]
        else:
            hf=50000000000000000000000000000000000000000000000000000000
            
        if(abs(h-hf)<0.000001):
            if(k==3):
                
                sum+=sim13(abs(h),abs(f[j-3]),abs(f[j-2]),abs(f[j-1]))
                plt.fill_between(x[j-3:j],f[j-3:j],color='red',label='simson 1/3')
                s1=s1+1
                k=k-1
            else:
                k=k+1
        else:
            if(k==1):
                
                sum+=Trap(abs(h),abs(f[j-1]),abs(f[j]))
                
                plt.fill_between(x[j-1:j + 1],f[j-1:j + 1],color='green')
                t=t+1
            else:
                if(k==2):
                    sum+=sim13(abs(h),abs(f[j-2]),abs(f[j-1]),abs(f[j]))
                    plt.fill_between(x[j-2:j + 1],f[j-2:j + 1],color='red')
                    s1=s1+1
                else:
                    sum+=sim38(abs(h),abs(f[j-3]),abs(f[j-2]),abs(f[j-1]),abs(f[j]))
                    plt.fill_between(x[j-3:j + 1],f[j-3:j + 1],color='yellow')
                    s3=s3+1
                k=1
        h=hf 
    return sum,t,s1*2,s3*3

            
    
        
sum1,t,s1,s3=unequally_space(N,x,f)
print("Trapezoidal rule:"+str(t)+" intervals")
print("1/3 rule: "+str(s1)+" intervals")
print("3/8 rule: "+str(s3)+" intervals")
print(sum1)






        
    
    