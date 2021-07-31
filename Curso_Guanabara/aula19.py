'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
print(pessoas)'''

'''brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]["uf"])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
'''Para copiar dentro de dicionários utilizar a função COPY.
o "[:} não funciona para dicionérios'''
for e in brasil:
#    print(e)
#    for v in e.values():
#        print(v)
    for k, v in e.items():
        print(f'O {k} é {v}')
#print(estado.values())
#print(estado.keys())
#    for k in e.keys():
#        print(k)
