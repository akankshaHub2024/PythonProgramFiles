my_dict={1:"Hello",2:"Good"}
my_dict[3]="Morning"
print(my_dict)
dict1={0:"a",1:"b",2:"c",3:"d"}
dict2={4:"e",5:"f",6:"g",7:"h"}
dict3={8:"i",9:"j",10:"k",11:"l"}
new_dict={**dict1,**dict2,**dict3}
print(new_dict)
new_dict1=dict1.copy()
new_dict1|=dict2
print(new_dict1)

