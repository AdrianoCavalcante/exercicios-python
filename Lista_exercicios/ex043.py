print('Vamos saber qual seu IMC')
print(30*"=")
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = int(peso/(altura**2))
print(f'Seu IMC é {imc:.2f}.')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 < imc <= 25:
    print('Você está no peso ideal!')
elif 25 < imc <= 30:
    print('Você está com sobrepeso!')
elif 30 < imc <= 40:
    print('Você está obeso!')
elif imc > 40:
    print('Você está cm obesidade mórbida!')
