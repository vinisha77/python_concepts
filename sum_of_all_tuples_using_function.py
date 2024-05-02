#Write a program that calculates the sum of all elements in a given tuple.

def myTuple(t):
    sum = 0
    for i in t:
        sum = sum + i
    return sum
    
given_tuple = (1,2,3,4)
total = myTuple(given_tuple)
print("The sum of all elements in given tuple is :",total)