from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano do seu nascimento com 4 digitos: '))
idade = (ano - nasc)
print(idade)
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif 9 < idade <= 14:
    print('Sua categoria é INFANTIL.')
elif idade <= 19 and idade > 14:
    print('Sua categoria é JUNIOR.')
elif idade <= 25:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categorie é MASTER')
