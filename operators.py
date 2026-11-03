#arithematic operator
'''a = 10
b = 3

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a % b)    # Modulus
print(a ** b)   # Power
print(a // b)   # division'''

#assignment operator
'''a = 10
a += 5
print(a)

a -= 3
print(a)

a *= 2
print(a)'''

#logical operator
'''a = 10
b = 5

print(a > 5 and b < 10)
print(a > 5 or b > 10)
print(not(a > 5))'''

#bitwise operator
'''a = 5   # 0101
b = 3   # 0011

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)'''

#membership operator
lst = [1, 2, 3, 4]

print(3 in lst)#in
print(5 not in lst)#not in

#identity operator
a = [1, 2, 3]
b=[2,3,1]
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)