# Write a function, flatten_array(), that takes in a 2-dimensional array,
# flattens it into a 1-dimensional array, and returns it.
# You can assume that you will only be given one or two-dimensional arrays

# For example, flatten_array([1, 2, [3, 4, 5], 6, [7, 8], 9])
# should return [1, 2, 3, 4, 5, 6, 7, 8, 9].


# flatten_array checks each element:
# If it is a list element, it stays the same.
# Otherwise, turn it into a list element.
# Sum all the lists together to make one array
def flatten_array(arr):
    return sum([[x] if type(x) != list else x for x in arr], [])


print(flatten_array([1, 2, [3, 4, 5], 6, [7, 8], 9]))

# Output
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
