# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:16:58 2019

@author: SAIKAT
"""

import numpy as np



 
f=open("in2.txt",'r')
lines_list=f.readlines()
s=lines_list[0]
s1=s.split(" ")
n=len(s1)

m=int(len(lines_list))-1

T=np.zeros([m+1,n+1])
T=np.matrix(T)


for i in range(0,m+1):
    s=lines_list[i]
    
    s1=s.split(" ")
    
    for j in range(0,n+1):
        if(i==0):
            if(j==n):
                T[i,j]=0
            if(j!=n):
                #print(s1[j])
                T[i,j]=(-1)*float(s1[j])
                #T[i,j]=format((-1)*float(s1[j]),'.2f')
        if(i!=0):
            T[i,j]=float(s1[j])
            
        
                
                
        


M=np.zeros([m+1,m+n+3],dtype=float)
M=np.matrix(M)
RM=m+1
CM=m+n+3
solcol=m+n+1
incol=solcol+1

hor_header=m+n+4
ver_header=m+1
hor_list=["Basic","Z"]
ver_list=["Z"]
variable_list=[]
variable_value=[]




def tableu(M,T):
    for i in range(0,m+1):
        for j in range(0,m+n+2):
            if(j==0 and i==0):
                
                M[i,j]=1
            if(i>0 and j==0):
                M[i,j]=0
            if(j>=1 and j<=n):
                M[i,j]=T[i,j-1]
            if(j>=(n+1) and j<=(m+n)):
                if(i==0):
                    M[i,j]=0
                if(i>0 and j==i+n):
                    M[i,j]=1
                if(i>0 and j!=i+n):
                    M[i,j]=0
            if(j==(m+n+1)):
                if(i==0):
                    M[i,j]=0
                if(i>0):
                    M[i,j]=T[i,n]
    return M



def isoptimal(M):
    
    for i in range(0,1):
        for j in range(0,n+m+1):
            if(M[i,j]<0):
                
                return False
    return True
def isBasic(col,hor_list,ver_list):
    for i in range(0,len(ver_list)):
        if(ver_list[i]==hor_list[col+1]):
            return True
    return False
        
        
        

def column_pivot(M,hor_list,ver_list):
    
    
    mini=M[0,0]
    
    for i in range(0,1):
        for j in range(0,m+n+1):
            if(mini>M[i,j] and isBasic(j,hor_list,ver_list)==False):
                mini=M[i,j]
    for i in range(0,1):
        for j in range(0,m+n+1):
            if(mini==M[i,j]):
                return j
                


def row_pivot(M):
    
    for i in range(0,m+1):
        if(M[i,incol]>0):
            mini=M[i,incol]
            break
    for i in range(0,m+1):
        if(M[i,incol]<mini and M[i,incol]>0):
            mini=M[i,incol]
    for i in range(0,m+1):
        if(M[i,incol]==mini):
            return i

def make_pivot_1(M,row,col):
   
    k=M[row,col]
    for i in range(0,solcol+1):
        
        
        M[row,i]=(M[row,i]/k)
       
        
         
            
        
        
            
def intercept(M,col):
    for i in range(0,m+1):
        M[i,m+n+2]=(M[i,m+n+1]/M[i,col])
    
def gaussJordan(M,row,col):
    for i in range(0,m+1):
        factor=(M[i,col]/M[row,col])
        if(i!=row):
            for j in range(0,solcol+1):
                M[i,j]=M[i,j]-(factor*M[row,j])


def table_col_Name(hor_list,hor_header):
    for i in range(2,hor_header):
        if(i>=2 and i<=(n+1)):
            hor_list.append("X"+str(i-1))
        if(i>=(n+2) and i<=(m+n+1)):
            hor_list.append("S"+str(i-n-1))
        if(i==(m+n+2)):
            hor_list.append("Sol")
        if(i==(m+n+3)):
            hor_list.append("Inter")
        

def table_row_Name(ver_list,ver_header):
    for i in range(1,m+1):
        ver_list.append("S"+str(i))
        
def XvariableName(n):
    for i in range(1,n+1):
        variable_list.append("X"+str(i))
def fvalue_of_variable(M,variable_list,ver_list):
    
    for i in range(0,len(variable_list)):
        isenter=0
        for j in range(0,len(ver_list)):
            if(ver_list[j]==variable_list[i]):
                variable_value.append(M[j,solcol])
                isenter=1
                break
        if(isenter==0):
            
            variable_value.append(0)
                
              
   
#update
XvariableName(n)
table_col_Name(hor_list,hor_header)
table_row_Name(ver_list,ver_header)


def printTable(M,hlist,vlist):
    s=""
    
    for i in range(0,len(hlist)):
        s+=str(hlist[i]+"\t")
    print(s)
    
    for i in range(0,RM):
        s1=vlist[i]+"\t"
        for j in range(0,CM):
            s1+=(str(format(M[i,j],'.2f'))+"\t")
        print(s1)
        
    
           
            

i=0 
M=tableu(M,T) 

print("step:1(Intial talble)")
print("\n")
printTable(M,hor_list,ver_list)
print("\n")



#step 2(1st part)

if(isoptimal(M)):
        print("step:2(1st Row element is nonegative")
        print("\n")
        printTable(M,hor_list,ver_list)
        print("\n")
        
        fvalue_of_variable(M,variable_list,ver_list)
        
        print("solution,Z(max) = "+str(format(M[0,solcol],'.2f')))
        for i in range(0,len(variable_value)):
            print("X"+str(i+1)+" = "+str(format(variable_value[i],'.2f')))


while((isoptimal(M))==False):
    
    
    #print("Iteration: "+str(i+1))
    #step 2(2nd part)  
    
    print("step:2(most negative coefficient finding)")
    print("\n")
    printTable(M,hor_list,ver_list)
    print("\n")
        
    col=column_pivot(M,hor_list,ver_list)
    
    #step 3
    intercept(M,col)
    print("step: 3(Intercept determination)")
    print("\n")
    printTable(M,hor_list,ver_list)
    print("\n")
    
    
    #step 4
    
    row=row_pivot(M)
    ver_list[row]=hor_list[col+1]
    
    print("step:4(Replace Basic by non basic) ")
    print("\n")
    printTable(M,hor_list,ver_list)
    print("\n")
    
    
    
    print("step:5(Making 1 pivot element)")
    make_pivot_1(M,row,col)
    print("\n")
    printTable(M,hor_list,ver_list)
    print("\n")
    
    print("step:5(Use jordan gauss)")
    gaussJordan(M,row,col)
    print("\n")
    printTable(M,hor_list,ver_list)
    print("\n")
    
    
    if(isoptimal(M)):
        print("step:2(1st Row element is nonegative")
        print("\n")
        printTable(M,hor_list,ver_list)
        print("\n")
        fvalue_of_variable(M,variable_list,ver_list)
        
        print("solution,Z(max) = "+str(format(M[0,solcol],'.2f')))
        
        for i in range(0,len(variable_value)):
            print("X"+str(i+1)+" = "+str(format(variable_value[i],'.2f')))
    
    
    

    
    
   
    

    
    
    
    
    
            
            
            
                
            




            
        
        
        
        
        
        
            












