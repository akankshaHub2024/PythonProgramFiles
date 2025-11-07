def remove_index(s,n):
    if n<0 or n>=len(s):
        return "Index is out of range"
    return s[:n]+s[n+1:]
str1="openAI"
print(remove_index(str1,3))