# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 01:49:28 2019

@author: SAIKAT
"""

import numpy as np
import matplotlib.pylab as plt

x=[]
y=[]
x1=[]
A=np.zeros((3,3),dtype=float)
A=np.matrix(A)
A2=np.zeros((4,4),dtype=float)
A2=np.matrix(A2)

B=np.zeros((3,1),dtype=float)
B=np.matrix(B)

B2=np.zeros((4,1),dtype=float)
B2=np.matrix(B2)

C=np.zeros((3,1),dtype=float)
C=np.matrix(C)

C2=np.zeros((4,1),dtype=float)
C2=np.matrix(C2)


f=open("data.txt",'r')

list_lines=f.readlines()
n=len(list_lines)
for i in range(0,n):
    s=list_lines[i];
    s1=s.split(" ")
    
    x.append(float(s1[0]))
    y.append(float(s1[1]))


def Curve_fit(x,y,n):
    sumx=0
    sumy=0
    sumxy=0
    sumx2=0
    sumx3=0
    sumx4=0
    sumx5=0
    sumx6=0
    sumx3y=0
    sumx2y=0
    st=0
    sr=0
    sr2=0
    sr3=0
    line1_y=[]
    line2_y=[]
    line3_y=[]
    for i in range(0,n):
        sumx=sumx+x[i]
        sumy=sumy+y[i]
        sumxy=sumxy+x[i]*y[i]
        sumx2=sumx2+x[i]**2
        sumx3+=x[i]**3
        sumx4+=x[i]**4
        sumx2y+=(x[i]**2)*y[i]
        sumx5+=x[i]**5
        sumx6+=x[i]**6
        sumx3y+=(x[i]**3)*y[i]
        
    xm=sumx/n
    ym=sumy/n
    
    
    a1=(n*sumxy-sumx*sumy)/(n*sumx2-sumx*sumx)
    a0=ym-a1*xm
    
    for i in range(0,n):
        st=st+(y[i]-ym)*(y[i]-ym)
        sr=sr+(y[i]-a1*x[i]-a0)*(y[i]-a1*x[i]-a0)
    r=((st-sr)/st)**(0.5)
    plt.scatter(x,y)
    for i in range(0,n):
        x1.append(x[i])
    x1.sort()
    for i in range(0,n):
        line1_y.append((a0+a1*x1[i]))
    
    
    print("\nFirst Order curve: \n")
    print("a0="+str(a0))
    print("a1="+str(a1))
    print("correlation coefficient="+str(r))
    
    
    
    #Second order
    
    A[0,0]=n
    A[0,1]=sumx
    A[0,2]=sumx2
    A[1,0]=sumx
    A[1,1]=sumx2
    A[1,2]=sumx3
    A[2,0]=sumx2
    A[2,1]=sumx3
    A[2,2]=sumx4
    
    B[0,0]=sumy
    B[1,0]=sumxy
    B[2,0]=sumx2y
    
    C=np.linalg.solve(A,B)
    a20=C[0,0]
    a21=C[1,0]
    a2=C[2,0]
    
    for i in range(0,n):
        line2_y.append((a20+a21*x1[i]+a2*x1[i]*x1[i]))
        
    
    
    for i in range(0,n):
        #st=st+(y[i]-ym)*(y[i]-ym)
        sr2=sr2+(y[i]-a21*x[i]-a20-a2*x[i]*x[i])*(y[i]-a21*x[i]-a20-a2*x[i]*x[i])
    r2=((st-sr2)/st)**(0.5)
    
    print("\nSecond Order Line: \n")
    print("a0="+str(a20))
    print("a1="+str(a21))
    print("a2="+str(a2))
    
    print("correlation coefficient="+str(r2))
    
    
    
    
    #Second order operation finish
    
    #Third order start
    
    for i in range(0,3):
        for j in range(0,3):
            A2[i,j]=A[i,j]
   
    
    
    A2[0,3]=sumx3
    A2[1,3]=sumx4
    A2[2,3]=sumx5
    A2[3,3]=sumx6
    A2[3,0]=sumx3
    A2[3,1]=sumx4
    A2[3,2]=sumx5
    
    B2[0,0]=sumy
    B2[1,0]=sumxy
    B2[2,0]=sumx2y
    B2[3,0]=sumx3y
    
    
    C2=np.linalg.solve(A2,B2)
    
    a30=C2[0,0]
    a31=C2[1,0]
    a32=C2[2,0]
    a3=C2[3,0]
    
    for i in range(0,n):
        line3_y.append((a30+a31*x1[i]+a32*x1[i]*x1[i]+a3*x1[i]*x1[i]*x1[i]))
        
        
    for i in range(0,n):
        
        sr3=sr3+(y[i]-a31*x[i]-a30-a32*x[i]*x[i]-a3*x[i]*x[i]*x[i])*(y[i]-a31*x[i]-a30-a32*x[i]*x[i]-a3*x[i]*x[i]*x[i])
    r3=((st-sr3)/st)**(0.5)
    
    print("\nThrid order Equation: \n")
    print("a0="+str(a30))
    print("a1="+str(a31))
    print("a2="+str(a32))
    print("a3="+str(a3))
    
    print("correlation coefficient="+str(r3))
    
    
    plt.plot(x1,line1_y,color='black',label='1st Order curve')
   
    plt.plot(x1,line2_y,color='blue',label='2nd Order curve')
    
    plt.plot(x1,line3_y,color='red',label='3rd Order curve')
    
    plt.xlabel("Abscissa (x) --->")
    plt.ylabel("Ordinat (y) --->")
    plt.title("Curve fitting graph")
    plt.legend()
    plt.grid()
    
     
    
    
Curve_fit(x,y,n)
    
        
