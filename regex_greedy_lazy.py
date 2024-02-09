import re
text = "The quick brown fox jumps over 12 lazy dogs."
# Find any word of at least 4 characters
# {4,} is a greedy match
print(re.findall(r"\b\w{4,}\b", text))
# Find 'o' followed by one or more 'g's
print(re.findall(r"og+", text))