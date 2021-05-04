a, b, *c = 10, 20, 'a', 'b'

def func1(a, b, *c):
    pass

func1(10, 20, 'a', 'b')  # c= ('a', 'b')

def func1(a, b, *args):
    pass

# *args exhausts positional arguments

def func1(a, b, *args, d):
    pass

# func1(10, 20, 'a', 'b', 100) - nao funcionará

def func1(a, b, c):
    pass

l = [10, 20, 30]

func1(*l)

a, b, *c = 10, 20, 'a', 'b'
print(c)

def func2(a, b, *c):
    print(a)
    print(b)
    print(c)

func2(10, 20)

func2(10, 20, 1, 2, 3)  # c será a tupla 1, 2, 3

def avg(*args):
    print(args)
    count = len(args)
    total = sum(args)
    return count and total/count
    # se count = 0 será F e, em conseq, exp. lógica será F.
    #if count == 0:
    #    return 0
    #else:
    #    return total/count


avg()
avg(10, 20)
print(avg(2, 2, 4, 4))


def avg(a, *args):
    print(args)
    count = len(args) + 1
    total = sum(args) + a

avg(2, 2, 4, 4)


def func3(a, b, c, *args):
    print(a)
    print(b)
    print(c)
    print(args)

l = [10, 20, 30, 40, 50]

# func3(l) --> errado.

func3(l, 'a', 'y')
func3(*l)

# Keyword Arguments

def func_5(a, b, c):
    pass

# Não é necessário manter a ordem
func_5(a=1, c=3, b=2)


# Mandatory keyword arguments

def func_6(a, b, *args, d):
    pass

# In this case, *args effectively exhausts all position arguments and d must be passed
# as a keyword (named) argument.

func_6(1, 2, 'x', 'y', d=100)
func_6(1, 2, d= 100)

# pode passar tudo mas se espera um keyword argument
def func_7(*args, d):
    pass

func_7(1, 2, 3, d=100)
func_7(d=100)


# We can force no positional arguments at all:

def func_8(*, d):
    pass

#func_8(1, 2, 3, d= 100) - exception
func_8(d = 100)


## ---------------------------------

def func_9(a, b=1, *args, d, e=True):
    pass

def func_10(a, b=1, *, d, e=True):
    pass

"""
 a -> mandaotory position argument (may be specificied using a named argument)
 b -> optional positional argument (may be specificied positionally, as a
 named argument, or not all), defautls to 1.
 args: catch-al for any(optional) additional positional arguments
 *: no additional positional arguments allowed
 d -> mandatory keyword argument
 e -> optional keyword argument, defaults to True.
"""






























