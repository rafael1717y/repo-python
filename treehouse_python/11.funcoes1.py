
def print_name():
    print("nome")


def print_favorite_movie():
    print("Mean Girls")

# escopo
num = 10

def set_num():
    num = 5
    print("num is {} in the local scope".format(num))

set_num()

def add_two_nums(num1, num2):
    val = num1 + num2
    return val

print(add_two_nums(5, 10))

# PACKING E UNPACKING

def packer(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

def packer2(*args):
    #print(args)
    for val in args:
        print(val)


#print(packer("hi", "i", "love", "python"))

## convertidos para um tupla
print(packer2("hi", "i", "love", "python"))





























