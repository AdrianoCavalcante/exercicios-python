preco = float(input('Qual o preço do produto? R$ '))
print('''Qual a forma de pagamento?
[ 1 ] à vista em dinheiro ou cheque (desconto 10%)
[ 2 ] à vista no cartão (desconto de 5%)
[ 3 ] em até 2 vezes no cartão de crédito (sem desconto)
[ 4 ] em 3 ou mais vezes no cartão de crédito (20 % de juros)''')
print(10*'.....')
final = int(input('Digite o número do índice da forma de pagamento (1, 2, 3 ou 4): '))
if final == 1:
    print(f'Desconto: R$ {preco*0.1:.2f}\nTotal a pagar: R$ {preco*0.9:.2f}')
elif final == 2:
    print(f'Desconto: R$ {preco*0.05:.2f}\nTotal a pagar: R$ {preco*0.95:.2f}')
elif final == 3:
    print(f'Total a pagar: R$ {preco:.2f}\n2 parcelas de {preco/2:.2f}')
elif final == 4:
    vezes = int(input('Quantas parcelas? '))
    print(f'Juros de R$ {preco*0.2:.2f}\nTotal a pagar: R$ {preco*1.2:.2f}\n{vezes} parcelas de R$ {preco*1.2/vezes:.2f}')
else:
    print('opção inválida, tente novamente!')
