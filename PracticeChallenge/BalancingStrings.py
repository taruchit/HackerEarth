# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:03:54 2021

@author: pc
"""

#Computation
def Result(S):
    K=0
    for s in S:
        if s=='(':
            K=K+1
        else:
            K=K-1
    '''        
    subStringList=list()
    if K==1:
        index=0
        
        for s in S:
            subString=S
            if s == '(':
                temp=subString.replace('(','',index)
                subStringList.append(temp)
                index=index+1
            else:
                index=index+1
                
    else:
        index=0
        
        for s in S:
            subString=S
            if s == ')':
                temp=subString.replace(')','',index)
                subStringList.append(temp)
                index=index+1
            else:
                index=index+1
    
    subStringSet=set()
    subStringSet=set(subStringList)
    res=len(subStringSet)
    return res
    '''
    if K>0:
        return K
    else:
        return K*(-1)

#User Input
S=input()

#Output
res=Result(S)
print(res)