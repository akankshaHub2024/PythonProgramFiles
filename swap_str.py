'''
12. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz'
'''
def swapstr(str1,str2):
    firststr=str1[:2]
    secstr=str2[:2]
    print(secstr+str1[2:]+" "+firststr+str2[2:])
swapstr('abc', 'xyz' )
