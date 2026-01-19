'''
while loop: Iterates over a block of code as long as a specified condition is true. 
Example:
counter = 0
while counter < 5:
    print("Hello world!")
    counter += 1
'''
'''
Read two integers start and stop variables
Display all even numbers between start and stop (inclusive)
Input : 1 10
Output : 2 4 6 8 10
'''
'''
start,stop = map(int,input("Enter start and stop values: ").split())
counter = start
while counter<=stop:
    if counter % 2 == 0:
        print(counter, end=" ")
    counter += 1
'''
'''
#FizzBuzz Problem
start,stop = map(int,input("Enter start and stop values: ").split())
while start<=stop:
    if start%3==0 and start%5==0:
        print("fizzbuzz")
    elif start%3==0:
        print("fizz")
    elif start%5==0:
        print("buzz")
    else:
        print(start)
    start+=1
    '''
'''
for loop: Used for iterating over a sequence (like a list, tuple, dictionary, set, or string).
Example:
for i in range(0,5,1):
    print("Hello world!")
    '''
'''
Display N natural numbers using for loop
'''
'''
N = int(input("Enter a value for N: "))
for i in range(1,N+1,1):
    print(i, end=" ")
    '''


'''
N = int(input("Enter a value for N: "))
for i in range(N,0,-1):
    print(i, end=" ")
'''

