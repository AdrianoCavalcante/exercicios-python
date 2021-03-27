credito = float(input('Qual valor você precisa? '))
renda = float(input('Qual sua renda mensal? '))
prazo = float(input('Em quantos anos pretende pagar? '))
parcela = float(credito / (prazo * 12))

print('Sua prestação mensal será de R$ {:.2f} para este prazo!'.format(parcela))

if parcela <= renda*0.3:
    print('O emprestimo pode ser concedino!')
#elif parcela > renda*0.3:
else:
    print('Infelizmente sua renda não comporta este valor de parcela!')