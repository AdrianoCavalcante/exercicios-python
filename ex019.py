from random import choice
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('digite o numero do terceiro aluno: ')
a4 = input('digite  nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
print(f'O aluno escolhido foi {choice(lista)}!')
