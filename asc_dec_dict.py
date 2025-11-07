my_dict = {'apple': 10, 'banana': 2, 'orange': 5}

# Step 1: Convert to list of tuples
items = []
for key in my_dict:
    items.append((key, my_dict[key]))

# Step 2: Sort manually (Ascending)
n = len(items)
for i in range(n):
    for j in range(0, n - i - 1):
        if items[j][1] > items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

# Step 3: Convert back to dictionary
asc_sorted_dict = {}
for item in items:
    asc_sorted_dict[item[0]] = item[1]

print("Ascending:", asc_sorted_dict)

# Step 4: Descending sort
# Use a copy of items or re-convert from my_dict
items = []
for key in my_dict:
    items.append((key, my_dict[key]))

# Bubble Sort (Descending)
n = len(items)
for i in range(n):
    for j in range(0, n - i - 1):
        if items[j][1] < items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

desc_sorted_dict = {}
for item in items:
    desc_sorted_dict[item[0]] = item[1]

print("Descending:", desc_sorted_dict)
