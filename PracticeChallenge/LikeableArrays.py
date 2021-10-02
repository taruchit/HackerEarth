# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 00:24:26 2021

@author: pc
"""

#Number of Testcases
T=int(input())

for t in range(T):
    #Number of elements in the list
    N=int(input())

    #Taking elements as input
    arr=input().split(" ")
    #print(type(arr))

    #Calculating frequency of elements in the list
    frequency=dict()
    for i in arr:
        if i in frequency:
            frequency[i]=frequency[i]+1
        else:
            frequency[i]=1

    #print(frequency)

    #Computation
    operations=list()
    for i in frequency:
        if(int(i)==int(frequency[i])):
            #print("i: ",int(i))
            #print("frequency[i]: ",int(frequency[i]))
            continue
        else:
            #Distance from the value
            temp1=int(i)
            temp2=int(frequency[i])
            #print("temp1 : ",temp1)
            #print("temp2 : ",temp2)
            a=temp1-temp2
            #print("a : ",a)
            #Distance from zero
            b=temp2
            #print("b : ",b)
            if(a<b):
                #print("a<b")
                operations.append(a)
            else:
                #print("b<a")
                operations.append(b)

    #print("operations: ",operations)

    res=min(operations)

    if(res<0):
        print(res*(-1))
    else:
        print(res)