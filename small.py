number=[44,85,64,12,33,10]
chota=min(number)
print(chota)
small=number[0]
for i in number:
    if small > i:
        small=i
print(small)
indices=[i for i,num in enumerate(number) if chota == num]
print(indices,chota)