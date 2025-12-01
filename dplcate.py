my_list = [1, 2, 3, 2, 4, 5, 1]

duplicates = []
seen = set()

for item in my_list:
    if item in seen:
        duplicates.append(item)
    else:
        seen.add(item)

print(duplicates)
