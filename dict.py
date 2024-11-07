# DICTIONARIES - {}
"A dictionary or dict is a mutable data structure that is a key/value pair"
"In a dict, you index by key."

student = {'name': 'Nengi', 'age': 40, 'sex': 'male', 'alive': True, 'score': 70.5}

## indexing - by key
# print(student['name'])
# print(student['sex'])

## Investigate items in a dict

# print(student.items())
# print(student.keys())
# print(student.values())

students = [{'name': 'Chibueze', 'age': 35, 'sex': 'male'},
            {'name': 'Nengi', 'age': 40, 'sex': 'male'},
            {'name': 'Ifeanyi', 'age': 45, 'sex': 'male'}]

# print(students[0]['name'])

students2 = {'names': ['Chibueze', 'Nengi', 'Ifeanyi'],
             'age': [35, 40, 45],
             'sex': ['male', 'male', 'male']}

# print(students2['names'][0])

## Adding and deleting items in a dict
# print(student)
# student['village'] = 'Okrika'
# print(student)

student2 = dict()
# print(student2)
# student2['name'] = 'Azaya'
# student2['age'] = 99
# student2['sex'] = 'trans-male'
# student2['alive'] = True
# print(student2)

# print(student)
# del student['alive']
# print(student)


student3 = dict(name='Tinubu', occupation='Renewed shege')
# print(student3)
# student3.clear()
# print(student3)

# print(student.keys())
# print(student['age'])
# print(student.get('age'))
# print(student.get('age', 'Key not found'))

# List or Dict comprehension - A way to dynamically create a list or dict
# a. list comprehension

x = [1, 2, 3, 4, 5]
y = [a**2 for a in x] # compute(a) for every 'a' in 'x'
z = [a/2 for a in x] # this should return .5, 1, 1.5, 2, 2.5

# b. dict comprehension

a = {chi: chi**2 for chi in x} # return same result as 'y' but as a dict

print(a)


b = {k: v*2 for k, v in a.items()} # from a dict
print(b)