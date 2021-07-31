jogador = dict()
gols = list()
soma = 0
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1, partidas+1):
    quantgols = int(input(f'    Quantos gols na partida {c}: '))
    gols.append(quantgols)
    soma += quantgols
jogador['gols'] = gols
#jogador['total'] = sum(gols) '''tbm poderia utilizar assim'''
jogador['total'] = soma
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-' * 30)
for cont, val in enumerate(jogador['gols']): # buscando a lista dentro do dicionário
    print(f'    => Na partida {cont+1}, fez {val} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
