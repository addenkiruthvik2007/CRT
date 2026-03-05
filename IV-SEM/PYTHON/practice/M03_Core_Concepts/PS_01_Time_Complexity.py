'''
Time complexity:the time required to run an algorithm based upon the input size.

O(1)-->Constant time 
O(n)-->Linear time 
O(n^2)-->Quadratic time 
O(log n)-->Logarithmic time 
O(n log n)-->Linearithmic time
O(2^n)-->Exponential time
'''
def constant_time(n):
    return n[0]
print(constant_time([10,20,30]))  #O(1)

def linear_time(n):
    for i in n:
        print(i)                #O(n)

def quadratic_time(n):
    for i in n:
        for j in n:
            print(i)
print(quadratic_time([10,20,30,40,50])            #O(n^2) 
      
def logarithmic_time(n):      
      return sorted(n)  
print(logarithmic_time([10,20,30,40,50,20])           #O(log n) 

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)            
n=int(input())
print(fib(n))           #O(2^n)        