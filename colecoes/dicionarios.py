

d = {'alice': '878', 'bob': '256-233'}
print(d['alice'])
d['alice'] = '98393843'

## Iterando em dicionários
## Função print pode aceitar mais de um argumento.
colors = {'crimson': 0xdc143c, 'coral': 0xff7f50}
for color in colors:
    print(color, colors[color]) ## usando o print para passar a chave e o valor