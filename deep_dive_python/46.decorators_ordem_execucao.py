def dec_1(fn):
    def inner():
        print('Running dec_1')
        return fn()
    return inner

def dec_2(fn):
    def inner():
        print('Running dec_2')
        return fn()
    return inner

@dec_1
@dec_2
def my_func():
    print("Running my_func")

#my_func = dec_1(dec_2(my_func))

my_func()



