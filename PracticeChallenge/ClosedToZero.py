# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 00:24:26 2021

@author: pc
"""

def Solve (N, A):
    min_val = min(i for i in A if i >= 0)
    res=int(min_val)
    return res
    # Write your code here
    
N = input()
A = list(map(int, input().split()))
out_ = Solve(N, A)
print (out_)