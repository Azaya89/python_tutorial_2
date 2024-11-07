# Function is a piece of contained code that does something specific

def greeting(name='World', curse=False):
    if curse:
        return f"{name.title()} you de crase"
    else:
        return f"I greet you specially, {name.title()}"
    
# print(greeting('obi', True))
# print(greeting("Buhari", curse=True))
# print(greeting(name="Buhari", curse=True))

# lambda function - is a short anonymous function that is usually used only once
## lambda argument:return expression

# def addition(x, y):
#     return f"The sum of {x} and {y} is {x+y}"

# print(addition(5, 3))

addition = lambda x,y: x+y

# print(addition(4,6))

students = [{'name': 'Chibueze', 'age': 35, 'sex': 'male'},
            {'name': 'Nengi', 'age': 40, 'sex': 'male'},
            {'name': 'Ifeanyi', 'age': 45, 'sex': 'male'}]
print(type(students))

def student_name(student):
    return student['name']

sorted_students  = sorted(students, key=lambda student: student['name'])
# print(sorted_students)