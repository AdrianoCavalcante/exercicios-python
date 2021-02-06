import math
ang = float(input('Digite um ângulo: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'O ângulo de {ang} tem o seno: {sen:.2f}, coseno: {cos:.2f} e tangente: {tan:.2f}')
