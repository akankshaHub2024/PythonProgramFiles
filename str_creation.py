# name1='w'
# if len(name1)>=2:
#     str1=name1[0:2]
#     str2=name1[-2:]
#     #print(str1+str2)
# else:
#     # print("")
def front_back_concat(s):
    return s[:2]+s[-2:] if len(s)>=2 else ''
print(front_back_concat("w3"))
print(front_back_concat("w3w3"))
print(front_back_concat("w3resource"))
