frase = 'Curso em Video Python'

print(frase)

print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(list)

print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso'in frase)

print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

tex ='      Aprenda Python   '
print(tex)
print(len(tex))
tex1 = (tex.strip())
print(tex1)
print(len(tex1))
print(tex.rstrip())
print(tex.lstrip())

frase1 = frase.split()
print(frase1)
frase2 = '-'.join(frase1)
print(frase2)