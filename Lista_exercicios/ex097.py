def escreva(txt):
    tam = int(len(txt) + 4)
    print('^' * tam)
    print(f'{txt: ^{tam}}')
    print('^' * tam)


# PROGRAMA PRINCIPAL
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
