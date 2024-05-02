 #Write a program that takes a string as input and prints its reverse.

def strFunct(t):
    reverse_str = t[::-1]
    return reverse_str


text = input("enter a string: ")
result=strFunct(text)
print("reversed string is",result)