# 1. LISTS - []
"A python list is a type of data structure that is mutable and can contain any type of data."
"In a list you index by position."

names = ['obi', 'ada', 'mike', 'chike', 'ayo']

# a. forward and reverse indexing - also works with sets and tuples
print(names[1])
# print(names[-4])

# b. slicing - select from 'start' to 'end-start' index
# print(names[2:5])
# print(names[:3])
# print(names[2:])
# print(names[:])

# c. reverse slicing
# print(names[-3::])

# d. sort and sorted - one sorts in-place, the other creates a new list.

# print(names)
# print(sorted(names))
# print(sorted(names, reverse=True))
# print(f"Original list: {names}")
# names.sort()
# print(f"List wey I use .sort(): {names}")
# print(names)


# e. append - add an item to the end of a list
# print(names)
# names.append('mojo')
# print(names)
# names.append('chacha')
# print(names)

# f. insert - add an item before index position in a list
# print(names)
# names.insert(1, 'mojo')
# print(names)
# names.insert(-1, 'chacha')
# print(names)

# g. pop - removes an item from list at index position
# print(names)
# names.pop()
# print(names)
# names.pop(1)
# print(names)

# h. adding and multiplying a list
print(names)
# names += ['dodo', 'jaja', 'kiki']
# print(names)

names *= 5
print(names)
