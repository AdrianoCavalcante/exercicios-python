nome = input('Digite seu nome: ')
nome1 = nome.strip()
nome2 = nome1.title()
nome3 = nome2.split()
nome4 = nome3[::-1]
print(f'Seu primeiro nome é {nome3[0]} e seu ultimo nome é {nome4[0]}!')
