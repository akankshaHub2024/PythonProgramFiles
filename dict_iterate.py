my_dict={0:"Hello",1:"Good",2:"Morning"}
for val in my_dict:
    print(val)
for val in my_dict.keys():
    print(val)
for data in my_dict.values():
    print(data)
for keys,data in my_dict.items():
    print(f"Key is {keys} and value is {data}")