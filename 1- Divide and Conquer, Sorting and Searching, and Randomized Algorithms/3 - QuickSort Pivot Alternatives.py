# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:58:53 2019

@author: Kiooola
"""

import numpy as np

def swap (arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]
    return arr

def partition (arr):
    pivot = arr[0]
    j=0
    
    for i in range(1,len(arr)):
        
        if arr[i]<pivot:
            arr = swap(arr,i,j+1)
            j +=1
        
    arr = swap(arr,0,j)
    return arr,j

def choose_pivot(arr,typ):

    if typ == "first":
        return 0
    
    elif typ == "last":
        return len(arr)-1
    
    elif typ == "median":
        
        if len(arr)%2 == 0:
            mid = int(len(arr)/2-1)
        else:
            mid = int(len(arr)/2)
    
        comp = [arr[0],arr[mid],arr[len(arr)-1]]
        median = int(np.median(comp))
        if median == comp[0]:
            return 0
        elif median == comp[1]:
            return mid
        elif median == comp[2]:
            return len(arr)-1
        
    elif typ == "random":
        return np.random.randint(0,len(arr)-1)
    
    else:
        raise ValueError ("invalid pivot selection type")
    

def quicksort(arr,typ):
    
    n = len(arr)
        
    if n>1:  
        p = choose_pivot(arr,typ)
        arr = swap(arr,0,p)        
        arr,p = partition(arr)
        
        arr[:p] , left_count = quicksort(arr[:p],typ)
        arr[p+1:] , right_count = quicksort(arr[p+1:],typ) 
        count = left_count + right_count + n-1
        
        return arr,count
    
    else:
        return arr,0

    


with open('QuickSort.txt') as f:
    arr = [int(x) for x in f]

print(quicksort(arr,"median"))
