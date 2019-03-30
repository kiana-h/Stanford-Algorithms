# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:12:36 2019

Stanford-Algorithms Specialization
PS1: recursive karatsuba multiplication

@author: Kiooola
"""
import math


def karatsuba(a,b):
    
    """
    this function calculates the product of two numbers based on this equation:
        xy = 10^n(ac) + 10^n/2((a+b)(c+d)-ac-bd) + bd
    where a and c are the first half of the given numbers, b and d are the second half.
    n is the number of digits.
    for example, if numbers are 1234 and 5678:
        a = 12 , b = 34 
        c = 56 , d = 78
    """
   
    #base case: if there's a single-digit number, multiply them
    if a<10 or b<10:
        return a*b
    
    #get the length of two numbers and pick the longer one to use in calcs 
    n = max(len(str(a)),len(str(b)))
    half_n = math.ceil(n/2)
    
    #split numbers in two
    a1 = int(a  / (10 ** (half_n)))
    a2 = int(a  % (10 ** (half_n)))
    b1 = int(b  / (10 ** (half_n)))
    b2 = int(b  % (10 ** (half_n)))   
    
    #recursively calculate 3 portions of the equation
    x1 = karatsuba(a1,b1)
    x2 = karatsuba((a1+a2),(b1+b2))
    x3 = karatsuba(a2,b2)
    
    return (10**n)*x1 +(10**(half_n))*(x2-x1-x3) + x3



    
print(karatsuba (3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))