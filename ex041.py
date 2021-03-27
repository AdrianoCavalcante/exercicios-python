from datetime import date
ano = int(date.today().strftime("%Y"))
nasc = int(input('Digite o ano do seu nascimento com 4 digitos: '))
idade = (ano-nasc)
print(idade)
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade <= 14 and idade > 9:
    print('Sua categoria é INFANTIL.')
elif idade <= 19 and idade > 14:
    print('Sua categoria é JUNIOR.')
elif idade == 20:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categorie é MASTER')
