'''Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''
str1="restart"
# char1=str1[0]
# inc=0
# for i in str1:
#     if i==char1 and inc>0:
#         i="$"
#     inc+=1
#     print(i,end="")
def replaceDef(str1):
    first_char=str1[0]
    finalStr=str1[1:].replace(first_char,"$")
    return first_char+finalStr
print(replaceDef(str1))
