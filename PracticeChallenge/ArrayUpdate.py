# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 19:36:31 2021

@author: pc
"""

#Input
N=int(input())
A=input().split(" ")

Arr=list()

for i in range(N):
    Arr.append(int(A[i]))
    
'''
Temporary check

print("N: ",N)
print("Arr: ",Arr)

'''

#Calculating the sum of elements
temp=0
for i in range(N):
    temp=temp+Arr[i]

'''
Temporary check

print("Sum of array elements: ",temp)

'''

n=temp//N

'''
Temporary check

print("Average value: - ",n)

'''

#Final answer
print(n+1)
