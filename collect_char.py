name="google.com"
from collections import Counter
print(Counter(name))
char_fre={}
for char in name:
    if char in char_fre:
        char_fre[char]+=1
    else:
        char_fre[char]=1
for char,count in char_fre.items():
    print(f"{char}:{count}")
