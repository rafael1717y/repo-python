arquivo = open('/home/rafael/PycharmProjects/repo-python/python_io/contatos1escrita.csv', encoding='latin_1', mode='a+')
print(type(arquivo.buffer))

# Lendo os arquivos do buffer
#conteudo = arquivo.buffer.read()
#print(conteudo)

texto_em_bytes = bytes('Esse é um texto em bytes', encoding='latin_1')
#print(texto_em_bytes) #b'Esse \xe9 um texto em bytes'
#print(type(texto_em_bytes)) #<class 'bytes'>


arquivo.close()

