frase = str(input('Digite uma frase para saber se é um Palindromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
tamlista = len(junto)
reversa = ''
#pode ser usado fatiamento ao invés do FOR, ex:
#reversa = junto[::-1]
for c in range(tamlista-1, -1, -1):
    reversa += junto[c]
if reversa == junto:
    print(f'A frase "{junto}" é um palindromo!')
else:
    print(f'A frase "{junto}" NÃO é um palindromo!')
