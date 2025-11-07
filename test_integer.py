'''Write a Python program to test whether an input is an integer.'''
def test_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
user_input=input("Please a value: ")
if test_integer(user_input):
    print("It is integer value")
else:
    print("It is not integer value")

