nome = str(input('Digite seu nome: '))
nome1 = nome.strip()
nome2 = nome1.title()
nome3 = nome2.split()
print(nome3)
quest = 'Silva' in nome2
print(f'O nome possue "Silva"? {quest}')