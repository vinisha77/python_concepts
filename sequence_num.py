"""Given a list of integers, return True if the sequence of numbers 1, 2, 3
appears in the list somewhere.
Example:
arrayCheck([1, 1, 2, 3, 1]) → True
arrayCheck([1, 1, 2, 4, 1]) → False
arrayCheck([1, 1, 2, 1, 2, 3]) → True"""

def arrayCheck(nums):
    # Iterate through the list until the third from last element
    for i in range(len(nums) - 2):
        # Check if the current triplet matches the sequence [1, 2, 3]
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False

# Test cases
print(arrayCheck([1, 1, 2, 3, 1]))  # True
print(arrayCheck([1, 1, 2, 4, 1]))  # False
print(arrayCheck([1, 1, 2, 1, 2, 3]))  # True
