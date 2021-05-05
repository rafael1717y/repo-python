def func1(a, b, c):
    print(a, b, c)

func1(1, 2, 3)
func1(1, c=3, b=2)
func1(c=3, b=2, a=1)

def func2(a, b, *args):
    print(a, b, args)

func2(1, 2, 3, 4)

def func3(a, b, *args, d):
    print(a, b, args, d)

func3(1, 2, 3, 4, d=5)

def func4(*args, d):
    print(args, d)

func4(1, 2, 3, d= 'a')
func4(d=4)

def func5(*, d):
    print(d)

func5(d=3)

def fun6(a, b, *, d):
    print(a, b, d)

fun6(1, 2, d=2)


def fun7(a, b=2, *args, d):
    print(a, b, args, d)

fun7(1, 5, 3, 4, d='a')


def fun8(a, b=20, *args, d=0, e):
    print(a, b, args, d, e)

fun8(5, 4, 3, 2, 1, e='all')

fun8(0, 600, d='good morning', e='python')

fun8(11, 'm/s', 24, 'mph', d='unladen', e='swallow')











