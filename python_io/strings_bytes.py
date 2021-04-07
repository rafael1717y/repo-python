# Impressão de path com raw_string (r')

path = r'C:\Users\Merlin\Documents\Spells'
print(path)


c = "oslo"
a = c.capitalize()
print(a)

#bytes
um_byte = b'some bytes'
print(type(um_byte))

norsk = "jeg begynner å le av å spise is når det er sol"
# convertendo para um bytes object
data = norsk.encode('utf8')
print(data)

norwegian = data.decode('utf8')
print(norwegian)
print(norwegian == norsk)