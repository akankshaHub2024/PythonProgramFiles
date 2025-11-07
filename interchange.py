'''
27. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
'''
def change(string):
    # If string is empty or has only one character, return it as is
    if len(string) <= 1:
        return string
    # Swap first and last characters, keep middle the same
    return string[-1] + string[1:-1] + string[0]

# Example usage
print(change("exchanged"))  # Output: 'dexchangd'
print(change("a"))          # Output: 'a'
print(change(""))           # Output: ''
