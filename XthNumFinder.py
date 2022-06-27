# Write a function, getX, that given an integer x and a list num returns the Xth number
# if the list was in sorted order. In other words, the Xth smallest number.
# Function Name: getX
# Input: An integer, x, and an unsorted list of integers nums that aren’t necessarily distinct
# Output: The integer corresponding to the Xth number in the sorted list

def getX(index, numList):
    return sorted(numList)[index] if index < len(numList) > 0 else 'List index is out of range.'


# Test Cases
print(getX(1, [6, 3, -1, 5]))
print(getX(1, []))
print(getX(4, [6, 3, -1, 5]))
