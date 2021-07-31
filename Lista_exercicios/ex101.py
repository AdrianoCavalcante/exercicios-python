from time import localtime


def votar():
    idade = int(localtime().tm_year) - ano
    print(f'Com {idade} anos: ', end='')
    if idade <= 15:
        return "Não vota!"
    elif 16 <= idade <= 17 or idade >= 65:
        return "Voto opcional!"
    else:
        return "Voto obrigatório!"


print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
print(votar())
