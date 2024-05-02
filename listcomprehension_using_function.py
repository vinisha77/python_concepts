# Write a program that takes a list of integers as input and uses list comprehension to create a new list 
#containing only the even numbers from the original list.



def list_funct(i):
    # Use list comprehension to create a new list containing only even numbers
    new_list = [x for x in i if x % 2 == 0]
    return new_list

# Take input from the user for the list of integers
input_list = [int(x) for x in input("Enter a list of integers separated by space: ").split()]

# Call the function to create a new list containing only even numbers
result = list_funct(input_list)

print("Even numbers from the original list:", result)
