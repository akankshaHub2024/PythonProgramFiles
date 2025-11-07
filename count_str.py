list_str= ['abc', 'xyz', 'aba', '1221']
count=0
for char in list_str:
    char1=char[0]
    char2=char[-1]
    if(char1== char2) and len(char)>=2:
        count+=1
        
print(count)
print(sum(1 for word in list_str if len(word)>=2 and word[0]==word[-1]))