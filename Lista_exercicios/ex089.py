turma = list()
aluno = list()
notas = list()
consulta = int()

"""O guanabara usou:
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 01: '))
    nota2 = float(input('Nota 02: '))
    media = ((nota1 + nota2)/2)
    turma.append([nome,[nota1, nota2],media])
    resp = str(input('Quer continuar? [ S / N ]')).strip().upper()[0]
    if resp == 'N':
        break"""

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 01: '))
    nota2 = float(input('Nota 02: '))
    notas.append(nota1)
    notas.append(nota2)
    aluno.append(nome)
    aluno.append(notas[:])
    aluno.append((nota1 + nota2)/2)
    notas.clear()
    turma.append(aluno[:])
    aluno.clear()
    resp = str(input('Quer continuar? [ S / N ]')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 30)
print(f'{"Nº":<5}{"NOME":<15}{"MÉDIA":<7}')
for c in range(0, len(turma), 1):
    print('-'*30)
    print(f'{c:<5}{turma[c][0].upper():<15}{turma[c][2]:<7.2f}')
print('-'*30)
while True:
    consulta = int(input('Mostrar as notas de qual aluno? (999 para sair): '))
    if consulta == 999:
        break
    elif consulta >= len(turma):
        print('Opção inválida!')
        print('-'*30)
    else:
        print(f'As notas de {turma[consulta][0]} são {turma[consulta][1]}.')
        print('-'*30)
print('Obrigado por usar, volte sempre!')
