 #Write a program that merges two dictionaries into a single dictionary.
 #If a key is common to both dictionaries, the value from the second dictionary should be used.

def funct(f,s):
    merged_dict = f.copy()
    merged_dict.update(s)
    return merged_dict


first_dict = {'a':1,'b':2,'c':3}
second_dict ={'d':4,'e':5,'b':10}

result =funct(first_dict,second_dict)
print("new merged dictionary is:",result)


