#nome = str(input('Digite seu nome: '))
#for c in nome:
#   print(c)
# TUPLAS SÃO IMUTÁVEIS

lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
#for cont in range(0, len(lanche)):
#    print(cont) """printa só o indice"""
#    print(lanche[cont])

#for comida in lanche:
#    print(comida)

for posicao, comida in enumerate(lanche):
    print(f'na posição {posicao} temos a comida {comida}')

#print(len(lanche))

print(sorted(lanche))
""" SORTED PARA COLOCAR OS ITENS DA TUPLA ORGANIZADOS POR ORDEM ALFABÉTICA"""
