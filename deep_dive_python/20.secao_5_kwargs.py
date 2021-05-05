"""
*args is used to scoop up variable amount of remaining positional arguments - tuple
* is the real performer here...args name is arbitrary

**kwargs is used to scoop up a variable amount of remaining keyword arguments - dict
** is the real performer
"""

def func(*, d, **kwargs):
    pass


func(d=1, a=2, b=3)
# d = 1 kwargs = {'a':2, 'b':3}

func(d=1) # d = 1 kwargs = {}

def func1(**kwargs):
    pass

func1(a=1, b=2, c=3)
func1() ## kwargs = {}

def func2(*args, **kwargs):
    pass

func2(1, 2, a=10, b=10)
# args = (1, 2)  e kwargs = {'a':10, 'b':20}

func2()

def func3(**others):
    print(others)


func3(a=1, b=2, c=3)

def func4(*args, **kwargs):
    print(args)
    print(kwargs)

func4(1, 2, x= 100, y=200)


def fn5(a, b, *, d, **kwargs):
    print(a)
    print(b)
    print(d)
    print(kwargs)

fn5(1, 2, x = 100, y = 200, d= 20)

































