def large_str(words, n):
    return [word for word in words if len(word) > n]

result = large_str(["name", "akanksha", "konda"], 3)
print(result)  # Output: ['name', 'akanksha', 'konda']
