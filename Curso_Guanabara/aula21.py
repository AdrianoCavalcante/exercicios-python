# INTERACTIVE HELP: PODEMOS AINDA ACESSAR PELO PYTHON CONSOLE O "HELP" OU OS COMANDOS NO PYCHARM
print(input.__doc__)
help(input)

# DOCSTRINGS: MANUAL DE UMA FUNÇÃO E OU INSTRUÇÃO DARA UTILIZAÇÃO (DOCUMENTAÇÃO)
# PARA CRIAR UMA DOCSTRING:

def contador(i, f, p):
    """
    -> FAZ UMA CONTAGEM E MOSTRA NA TELA.
    :param i: INÍCIO DA CONTAGEM
    :param f: FIM DA CONTAGEM
    :param p: PASSO DA CONTAGEM
    :return: SEM RETORNO
    AINDA PODEMOS INCLUIR QUALQUER MENSAGEM ADICIONAL MA DOCSTRING
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM')


help(contador)


# PARÂMETROS OPCIONAIS
def somar(a=0, b=0, c=0):   # PODEMOS DEFINIR VALORES PADRÕES PARA NOSSOS PARÂMETROS
    """
    :param a: PRIMEIRO VALOR
    :param b:SEGUNDO VALOR
    :param c:TERCEIRO VALOR
    :return:
    CASO NÃO DIGITADO NENHUM VALOR PARA ALGUMA DAS POSIÇÕES O VALOR PADRÃO É ZERO
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(3, 2)
somar()
print()


# ESCOPO DE VARÁVEIS:
""" VARIÁVEIS DEFINIDAAS DENTRO DE FUNÇÕES (DEF's) SÓ VALEM DENTRO DA FUNÇÃO, ENQUANTO AS 
VARIÁVEIS DEFINIDAS NO PROGRAMA PRINCIPAL PODE SER LIDA DENTRO DAS FUNÇÕES DESDE QUE NÃO 
SEJA REDEFINIDA DENTRO DA PRÓPRIA FUNÇÃO A MENOS QUE SEJA USADA DENTRO DA FUNÇÃOO O COMANDO
"global x" QUE IRÁ FAZER COM QUE A VARIÁVEL (X) SEJA RECONHECIDA TAMBEM NO PROGRAMA PRINCIPAL
E IRA IGNORAR A VARIÁVEL QUE SE REPETIR DENTRO DO PROGRAMA PRINCIPAL.
NÃO VALE PARA VARIÁVEIS QUE NÃO EXISTEM NO PROGRAMA PRINCIPAL"""


def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')
print()


def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')
print()


# RETORNO DE VALORES (return)
def somar(x=0, y=0, z=0):   # PODEMOS DEFINIR VALORES PADRÕES PARA NOSSOS PARÂMETROS
    s = x + y + z
    return s   # AO INVES DA FUNÇÃO IMPRIMIR UM RESULTADO PODEMOS PEDIR PARA ELA RETORNAR UM RESULTADO


r1 = somar(3, 2, 5)
r2 = somar(3, 2)
r3 = somar()
print(f'Os resultados foram {r1}, {r2} e {r3}')   # PODEMO ENTÃO IMPRIMIR OS RETORNOS COM A FORMATAÇÃO QUE QUISERMOS
print()


def fatorial(numer=1):
    f = 1
    for c in range(numer, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
if par(n):
    print('É par!')
else:
    print('Não é par!')
