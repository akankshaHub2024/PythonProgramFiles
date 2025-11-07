'''28. Write a Python program to remove the characters which have odd index values of a given string.
'''
def remove_odd_index(string):
    # Using string slicing to get even indices characters
    return string[::2]

result = remove_odd_index("characters")
print(result)  # Output: 'caaes'
