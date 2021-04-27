course = {'teacher' : 'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginner'}

print(course['teacher'])

# ordem lexográfica

print(course.keys())
print(course.values())

# Extraindo o dicionário
print(sorted(course.keys()))

course['teacher'] = 'Treasure'
course['level'] = 'intermediate'
print(course)

## Adiciona um novo key, value pair ao dicionário
course['stages'] = 2
print(course)

del(course['stages'])
print(course)

#for item in course:
#    print(course[item])

print(course.items())

for key, value in course.items():
    print(key)
    print(value)

def print_teacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')


print_teacher(name='Ashley', job='Instructor', topic='Python', second_topic = 'javascript')






















