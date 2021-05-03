def process(s):
    print('intial s # = {0}'.format(id(s)))
    s = s + ' world'
    print('final s # = {0}'.format(id(s))) # após modificar s o valor do end de memória é outro

my_var = 'hello'
print('my_var # = {0}'.format(id(my_var)))

print(process(my_var))

print(id(my_var))

def modify_list(lst):
    print('intial s # = {0}'.format(id(lst)))
    lst.append(100)
    print('final s # = {0}'.format(id(lst)))  ## end memória continua o msm

print("+++")
my_list = [1, 2, 3]
print(id(my_list))

print(modify_list(my_list))

print(id(my_list))

def modify_tuple(t):
    print('intial s # = {0}'.format(id(t)))
    t[0].append(100)
    print('final s # = {0}'.format(id(t)))

print('## tuple ##')
my_tuple = ([1, 2], 'a')
print(id(my_tuple))

print(modify_tuple(my_tuple))

print(my_tuple)







