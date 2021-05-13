class Protected:
    __name = 'Security'

    def __method(self):
        return self.__name


prot = Protected()
#print(prot.__name)

print(dir(prot))
#print(prot._Protected_method())