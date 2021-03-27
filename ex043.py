print('Vamos saber qual seu IMC')
print(30*"=")
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = int(peso/(altura*altura))
print(f'Seu IMC é {imc:.2f}.')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc > 18.5 and imc <= 25:
    print('Você está no peso ideal!')
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso!')
elif imc > 30 and imc <= 40:
    print('Você está obeso!')
elif imc > 40:
    print('Você está cm obesidade mórbida!')
