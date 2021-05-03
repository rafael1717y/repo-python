"""
a = int(10)
a = int(-10)

a = int(10.9) -> truncation: a -> 10
a = int(-10.9) -> truncation: a -> 10
a = int(True) -> 1
a = int(Decimar("10.9")) -- truncation: a -> 10

a = int("10") -> 10
"""

a = int("10")
print(a)

# Se a base não é especificada, o padrão é base 10. A base deve estar entre 2 a 36.
b = int("123")
print(b)

c = int("1010", base=2)  # 10
print(c)

d = int("A12F", base=16)  #41263 em base 10
print(d)

e = int("A", base=11)
print(e)

# built-in functions: bin()  bin(10) -> '0b1010', oct(10) -> '0o12', hex()

f = 0b1010
print(f)

g = 0o12
print(g)











