# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 18:40:32 2021

@author: pc
"""

def findingPrimeFactors(n):
    fact=list()
    #Prime number
    d=2
    while(n>1):
        k=0
        print("n : ",n)
        while(n%d==0):
            n=n/d
            k=k+1
        if(k>0):
            fact.append(d)
            print("d: ",d)
        d=d+1
    return fact    

#Taking inputs for two integers
a=int(input())
b=int(input())

factorsA=list()
factorsA=findingPrimeFactors(a)
print("factorsA: ",factorsA)

factorsB=list()
factorsB=findingPrimeFactors(b)
print("factorsB: ",factorsB)

set_A=set(factorsA)
set_B=set(factorsB)

#Finding the common elements
Res=set_A & set_B

print(Res)

print("Final answer: - ")
print(len(Res)+1)
