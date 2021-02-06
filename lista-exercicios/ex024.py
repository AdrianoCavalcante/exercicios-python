cidade = str(input('Digite o nome de uma cidade: '))
cidade1 = cidade.strip()
cidade2 = cidade1.title()
cidade3 = cidade2.split()
cidade4 = cidade3[0]
print(cidade2)
a = cidade4=='Santo'
print(f'O nome da cidade começa com "Santo"? {a}')