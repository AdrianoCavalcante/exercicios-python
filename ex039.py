from datetime import date
nasc = int(input('INFORME O ANO DO SEU NASCIMENTO COM 4 DIGITOS: '))
ano = int(date.today().strftime("%Y"))
idade = (ano - nasc)
print(f'Este ano voc completa {idade} anos.')
if idade < 18:
    print(f'Ainda não é o seu ano de alistamento militar!\nPoderá se alistar em {18-idade} anos')
elif idade == 18:
    print('Este é o ano do seu alistamento militar!')
elif idade > 18:
    print(f'Já passou o ano do seu alistamento militar!\nSe não se alistou, está {idade-18} anos atrasedo')
