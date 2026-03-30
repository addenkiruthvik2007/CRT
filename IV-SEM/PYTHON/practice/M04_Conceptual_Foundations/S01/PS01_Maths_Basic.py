'''' 
import math
print(min([1,2,3,4]))
print(max([1,2,3,4]))
print(sum([1,2,3,4]))
print(abs(12))#absolute_value
print(abs(-10))
#print(dir(math))
print(math.factorial(5))
#GCD of two numbers 
'''
'''
8->1,2,4,8
10->1,2,5,10 
2 is the greatest common factor 
''' 
#sol1
'''
a=int(input())
b=int(input())
min_num=min(a,b)
gcd=1
for i in range(1,min_num+1):
    if a%i==0 and b%i==0:
        gcd=i 
print(gcd)        
'''
#sol2
a=int(input())
b=int(input())
gcd=1
while b!=0:
    a,b=b,a%b 
print(a)
