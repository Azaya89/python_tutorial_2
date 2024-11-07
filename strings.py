# PYTHON DATA TYPES
# Strings
# Integer
# Floating Point numbers
# Boolean

# Strings
## String methods
# a - title()
name = 'isaiah'
name2 = 'bimbo'
# print(name2)
# print(name2.title()) # first one

# b - upper()
# print(name.upper()) # second one

# c - lower()
name3 = 'JOHN'
# print(name3.lower()) # third one

# d - replace()
# print(name.replace('a', 'y'))
# print(name.replace('a', 'z', 1))
name4 = 'haaland'
# print(name4.replace('a', 'y', 2)) # 4th one

# e - split()
name5 = 'banana'
print(name5.split('a', 2)) # 5th one

names  = 'obi ada chike tinubu'
# print(names.split())
# print(names.split('i',2))

# f - strip()

name6 = "  ojukwu  "
# print(name6) # 6th one
# print(name6.strip())
# print(name6.lstrip())
# print(name6.rstrip())

name_format = name6.strip().title()
# print(name_format)

# input function
name7 = input("What is your name: ")
name7 = name7.strip().title()

# f-string aka format-string
greeting = f"Good morning, {name7}. You are welcome to this class!"
print(greeting)