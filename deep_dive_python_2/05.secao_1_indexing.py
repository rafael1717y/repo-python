"""
seq[i:j]
if i > len(seq) -> len(seq)
if j > len(seq) -> len(seq)

if i < 0 -> max(0, len(seq) + i)
if j < 0 -> max(0, len(seq) + i)

i omitted or None -> 0
j omitted or None -> len(seq)

[i:j:k] = {x = i + n * K | 0 <= n < (j-i)/k }

k > 0 the indices are: i, i+k, i+2k, i+3k, ..., <j

"""

l = [1, 2, 3, 4, 5]
print(l[0:2])
l[0:2] = ('a', 'b', 'c')

s = slice(0, 2)
l = [1, 2, 3, 4, 5]
print(l[s])


l = ['a', 'b', 'c', 'd', 'e', 'f']

# We can specify slices that are "out of bounds"
print(l[3:100]) # No error !
print(l[-3: -1])

# When not specified, the step value defaults to 1
print(l[0:6:2])
print(l[1:15:3])
print(l[-1:-4:-1])


l = ['a', 'b', 'c', 'd', 'e', 'f']
print(slice(10, -5, -1).indices(6))

s = slice(0, 2)
print(type(s)) # class slice

print(s.start)
print(s.stop)


data = []
for row in data:
    first_name = row[0:51]
    last_name = row[51:101]
    ssn = row[101:111]


range_first_name = slice(0, 51)
range_last_name = slice(51, 101)
range_ssn = slice(101, 111)

data = []
for row in data:
    first_name = row[range_first_name]
    last_name = row[range_last_name]
    ssn = row[range_ssn]


l = 'python'
print(l[0:1])
print(l[0:600])
print(l[0:6:2])

# .slice()
s1 = slice(0, 6, 2)
print(l[s1])

s1 = slice(None, 4)
print(l[s1])

start = None
print(l[start:4])
print(l[3:])
print(l[3:0:-1])
print(l[3:-1:-1])





s = slice(1, 5)
print(s.start)

# Ìndices da sequencia
print(s.indices(4))
print(s.indices(10))

print(list(range(1, 5, 1)))

slice(0, 100, 2).indices(10)
print(list(range(0, 10, 2))) # [0, 2, 4, 6, 8]

t = slice(0, 100, 2).indices(10)

print(range(*t))
print(list(range(*t)))

start = 5
stop = 10
step = 2
length = 100

print(list(range(*slice(start, stop, step).indices(length))))
print(l[::-1])