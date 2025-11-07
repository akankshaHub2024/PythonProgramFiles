str1="akanksha konda"
print(len(str1))
count=0
for i in str1:
    count+=1
print(count)
from collections import Counter
char_count=Counter(str1)
print(char_count)