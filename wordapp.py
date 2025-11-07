'''
13. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing' 
Sample String : 'string'
Expected Result : 'stringly'
'''
def addsuffix(str1):
    if len(str1)>=3:
        last_char=str1[-3:]
        if last_char == "ing":
            result=str1+"ly"
        else:
            result=str1+"ing"
        print(result)
addsuffix("abc")
addsuffix("string")
def add_suffix(str1):
    if len(str1) < 3:
        return str1
    elif str1.endswith("ing"):
        return str1 + "ly"
    else:
        return str1 + "ing"

# Sample usage
print(add_suffix("abc"))     # Output: abcing
print(add_suffix("string"))  # Output: stringly
print(add_suffix("go"))      # Output: go
