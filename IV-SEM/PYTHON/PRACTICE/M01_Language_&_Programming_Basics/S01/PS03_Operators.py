a = 10
b = 3

print("ARITHMETIC OPERATORS")
print( a + b) #13
print( a - b) #7
print( a * b) #30
print( a / b) #3.3333
print( a % b) #1
print( a // b) #3
print( a ** b) #1000

print("\nRELATIONAL OPERATORS")
print( a == b) #False
print( a != b) #True
print( a > b) #True
print( a < b) #False
print( a >= b) #True
print( a <= b) #False

print("\nLOGICAL OPERATORS")
print( a > 5 and b < 5) #True
print( a > 5 or b > 5) #True
print( not(a > 5)) #False

print("\nASSIGNMENT OPERATORS")
c = 5
print( c) #5
c += 2
print( c) #7
c -= 1
print( c) #6
c *= 2
print( c) #12
c /= 2
print( c) #6.0

print("\nBITWISE OPERATORS")
print( a & b) #2
print( a | b) #11
print( a ^ b) #9
print( ~a) #-11
print( a << 1) #20
print( a >> 1) #5

print("\nMEMBERSHIP OPERATORS")
s = "python"
print( 'p' in s) #True
print('z' not in s) #True

print("\nIDENTITY OPERATORS")
x = 10
y = 10
print( x is y) #True
print( x is not y) #False
