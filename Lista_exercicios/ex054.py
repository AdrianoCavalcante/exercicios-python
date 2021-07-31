from datetime import date
hoje = date.today()
quant1 = 0
quant2 = 0
for c in range(1, 8):
    dia = int(input(f'Didite o dia do aniversário da {c}ª pessoa: '))
    mes = int(input(f'Didite o mês de anirversário da {c}ª pessoa: '))
    ano = int(input(f'Didite o ano de nascimento da {c}ª pessoa: '))
    data = date(ano, mes, dia)
    idade = (date.today() - data)
    idade2 = str(idade).split(' ')[0]
    idade3 = int(idade2)
    if idade3 >= 21*365:
        quant1 += 1
    else:
        quant2 += 1
print(f'{quant1} pessoas tem mais de 21 anos')
print(f'{quant2} pessoas NÃO ainda não tem 21 anos')
