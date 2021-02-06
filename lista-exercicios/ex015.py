qd = float(input('Quantos dias o veículo ficou alugado? '))
qkm = float(input('Quantos quilômetros foram percorridos no período? '))
valor = qd*60+qkm*0.15
print(f'O valor a pagar pela locação é R${valor:.2f}.')