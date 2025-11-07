'''31. Write a Python function that takes two lists and returns True if they have at least one common member. '''
def have_common_member(list1, list2):
    # Convert one list to a set for faster lookup
    set1 = set(list1)
    # Check if any element in list2 is in set1
    for item in list2:
        if item in set1:
            return True
    return False

# Example usage
print(have_common_member([1, 2, 3], [4, 5, 3]))  # True
print(have_common_member(['a', 'b'], ['c', 'd']))  # False
