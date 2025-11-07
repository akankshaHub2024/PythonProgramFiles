list1=[1,2,3,4,5,6]
print(list1)
list1.append(7)
print(list1)
list1.remove(7)
print(list1)
list1.pop(3)
print(list1)
list2=[50,20,10]
list1.extend(list2)
print(list1)
list1.insert(3,"hello")
print(list1)
'''
List Methods
append
expand
remove
pop
insert
index
clear
count
sort
reverse
copy
'''
l1=[8,7,5,6,9,8,8,1] 
l1.remove(8)
print(l1)
#remove all the 8 values from the list
l2=[x for x in l1 if x!=8]
print(l2)