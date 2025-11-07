number=[3,5,6,7,8,9,9]
print(max(number))
large=number[0]
for i in number:
    if large<i:
        large=i
print(large)
#Findng index of large number
index_list=[i for i,num in enumerate(number) if num==large]
print(index_list)