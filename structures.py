# python data structures
# lists
# dictionaries
# tuples
# sets

# 1. LISTS - []
"A python list is a type of data structure that is mutable and can contain any type of data."
"In a list you index by position."

things = ['obi', 23, 5.6, True]
list_of_things = [['ada', 25], ['obi', 32], ['bala', 45]]

# create lists
empty_list = []
create_list = list()

full_name = 'ifeanyi malawi obi'

name_list = list(full_name)

first_name, last_name, middle_name = full_name.split()
print(full_name.split())
print(first_name)
print(last_name)

# 2. DICTIONARIES - {}
"A dictionary or dict is a mutable data structure that is a key/value pair"
"In a dict, you index by key."

name_dict = {'name': 'Peter'}
empty_dict = {}
create_dict = dict()

dict_of_things = {'name' : 'ada', 'age': 25, 'sex': 'female'}
# print(dict_of_things.keys())

# Concept called index/indexing
"An index is the position of an item in an iterable. In python, we have 0 indexing"
#print(dict_of_things['age'])

# mutability
# print(things)
# print(things[0])

things[0] = 'ada'
# print(things)
# print(things[0])

things[2] = 2.5
# print(things)


# 3. TUPLES - ()
"A tuple is an immutable data structure. Like a list, it also has positional indexing and can contain any data type/structure"

name_tuple = ('obi', 10, 2.5, True)
# print(name_tuple)
# print(name_tuple[0])
# print(type(name_tuple))

empty_tuple = ()
create_tuple = tuple()

# name_tuple[0] = 'ada'
# print(name_tuple)


# 4. SETS
"A set is a mutable data structure that has unique items. Like a list, it also has positional indexing etc"

list_comp = ['obi', 20, 2.5, True, 20, 'obi']
set_of_things = {'obi', 20, 2.5, True, 20, 'obi'}

# print(list_comp)
# print(set_of_things)
# print(len(set_of_things))
create_set = set()

nigerian_names = ['obi', 'amaka', 'chike', 'amaka', 'obi']
# print(set(nigerian_names))