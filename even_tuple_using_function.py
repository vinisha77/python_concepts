 #Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.

def myTuple(t):
    new_tuple = ()  
    for i in t:
        if i % 2 == 0:
            new_tuple += (i,)  
    return new_tuple

tuple_elements = (1, 2, 3, 4, 5, 6)


result = myTuple(tuple_elements)

print("Tuple containing only the even numbers:", result)



"""def myTuple(t):
    return tuple(i for i in t if i % 2 == 0)

tuple_elements = (1, 2, 3, 4, 5, 6)

# Call the function to create a new tuple containing only even numbers
result = myTuple(tuple_elements)

print("Tuple containing only the even numbers:", result)"""


    
