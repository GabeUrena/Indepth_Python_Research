import math # this module lets you utilize math functions

#Algorithmic Operations
print("Algorithmic Operations using 10 and 3.")
print("Addition:",10+3)  #Addition
print("Subtraction",10-3)  #Subtraction
print("Multiplication",10*3)  #Multiplication
print("Division",10/3)  #Division
print("Floor Division",10//3) #Floor Division
print("Modulus",10%3)  #Modulus
print("Exponentiation",10**3) #Exponentiation
print("***************************************************")

#augmented assignment operator
x=10
x+=3 # this is the same as x = x + 3
print(x)

x = 10 + 3 * 2 # operator Precidence the mulitplication goes first
print(x)
# Order of precidence
# Parenthesis > First exponentiation > Multiplication or division > addition or subtraction
print("***************************************************")

#Math Functions
x = 2.9
print(round(x))
print(abs(-2.9))

print(math.ceil(2.9))
print(math.floor(2.9))

#https://docs.python.org/3/library/math.html


#This code was written by Gabriel Urena