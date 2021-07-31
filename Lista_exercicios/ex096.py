def area(larg, comp):
    a = larg * comp
    print(f'A área do seu terreno {larg:.2f} x {comp:.2f} é de {a:.2f}m²')


# PROGRAMA PRINCIPAL
print('  Controle de terrenos')
print('-' * 24)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
