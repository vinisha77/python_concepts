 #Write a program that takes two integers as input, base and exponent, and calculates the power using function.

def powerCal(base,exponent):
    result = 1
    for _ in range(exponent):
        
        result *= base
       # print(result)
    return result

base = int(input("enter a base: "))
exponent = int(input("enter a exponent: "))

res = powerCal(base,exponent)

print("The result of base {}  raised to the power of exponent {} is : {}".format(base,exponent,res))




