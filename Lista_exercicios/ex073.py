times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
            'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo',
            'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
            'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-='*30)
print(f'A clasificação do campeonato brasileiro de 2017 foi: {times}')
print('-='*30)
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('-='*30)
print(f'Os últimos quatro colocados são: {times[-4:]}')
print('-='*30)
print(f'Os times que participaram do campeonato brasileiro de 2017 foram: {sorted(times)}')
print('-='*30)
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª colocação.')
print('-='*30)