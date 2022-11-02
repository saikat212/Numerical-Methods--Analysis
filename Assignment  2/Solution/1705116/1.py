# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np


def LU(A,sz):
    for r in range(0,sz):
        for c in range(0,sz):
            if(c>r):
                key=(A[c,r]/A[r,r])
                L[c,r]=key
                for p in range(0,sz):
                    A[c,p]=A[c,p]-(key*A[r,p])
                    U[c,p]=A[c,p]
            if(c==r):
                L[r,c]=1
    return L,U
                    
            
                
            
    

f=open('in1.txt', 'r')

lines_list=f.readlines()
sz=int(lines_list[0])



A=np.zeros([sz,sz],dtype='float')
A=np.matrix(A)

B=np.zeros([sz,1],dtype='float')
B=np.matrix(B)

U=np.zeros([sz,sz],dtype='float')
L=np.zeros([sz,sz],dtype='float')
U=np.matrix(U)
L=np.matrix(L)



f=open("out1.txt","w+")

for i in range(0,sz):
    s=lines_list[i+1]
    s1=s.split(" ")
    for j in range(0,sz):
        A[i,j]=float(s1[j])
        U[i,j]=float(s1[j])


for i in range(0,sz):
    s=lines_list[i+sz+1]
    s1=s.split(" ")
    for j in range(0,1):
        B[i,j]=float(s1[j])
         
L,U=LU(A,sz)

def filewriting(f,M,r,c):
    
    for i in range(0,r):
        for j in range(0,c):
            f.write(("%.4f"% M[i,j]))
            f.write(" ")
        f.write("\n")
            
    f.write("\n")
    
    
    
def X_filewriting(f,M,r,c):
    
    for i in range(0,r):
        for j in range(0,c):
            f.write(("%.4f"% M[i,j]))
            f.write(" ")
        f.write("\n")
            
    
        
    

   
        

     
filewriting(f,L,sz,sz)
filewriting(f,U,sz,sz)


for i in range(0,sz):
    c=0
    for j in range(0,sz):
        
        if(U[i,j]==0):
            c=c+1
            
    
    if(sz==c):
        
        f.write("No unique solution")
        f.close()
        
        exit(1)
        
for i in range(0,sz):
    c=0
    for j in range(0,sz):
        
        if(U[j,i]==0):
            c=c+1
            
    
    if(sz==c):
        
        f.write("No unique solution")
        f.close()
        
        exit(1)

IN_L=np.linalg.inv(L)
IN_U=np.linalg.inv(U)
Y=IN_L*B
X=IN_U*Y
filewriting(f,Y,sz,1)
X_filewriting(f,X,sz,1)
f.close()

    
        

        
            






 



    
         
        
            



   
  
   
   

