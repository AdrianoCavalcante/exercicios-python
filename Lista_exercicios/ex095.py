equipe = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    soma = 0
    print('--' * 30)
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, partidas+1):
        quantgols = int(input(f'Quantos gols na partida {c}: '))
        gols.append(quantgols)
        soma += quantgols
    jogador['total'] = soma
    jogador['gols'] = gols[:]
    equipe.append(jogador.copy())
    gols.clear()
    while True:
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp in 'S N':
            break
        print('ERRO! Digite apenas S ou N' )
    if resp == 'N':
        break
print('=-' * 30)
print(' Cod. ', end=' ')
for k in jogador.keys():
    print(f'{k: <15}', end='')
print()
print('--' * 30)
for c, dados in enumerate(equipe):
    print(f'{c:3}', end='    ')
    for inf in dados.values():
        print(f'{str(inf):<15}', end='')
    print()
'''    print(f'{c: <3} {dados["nome"]: <20}', end='    ')
    print('{: <20}'.format(f'{dados["gols"]}'), end='')
    print(f'{dados["total"]: <20}')''' # substituido na correção
print('--' * 30)
while True:
    codigo = int(input('Mostrar dados de qual jogador? (999 para encerrar)'))
    if codigo == 999:
        break
    elif codigo >= len(equipe):
        print(f'ERRO! Não existe jogador com o código {codigo}! Tente novamente')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {equipe[codigo]["nome"]}:')
        for indce, dados in enumerate(equipe[codigo]["gols"]):
            print(f'   No jogo {indce+1}, fez {dados} gols.')
    print('--' * 30)
print('< < < V O L T E   S E M P R E > > >')
print('--' * 30)
