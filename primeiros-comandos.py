Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("estou aprendendo python")
estou aprendendo python
>>> print'Olá Mundo'
SyntaxError: invalid syntax
>>> print('Olá Mundo')
Olá Mundo
>>> 7+4
11
>>> print('7+4')
7+4
>>> print('7'+'4')
74
>>> print(7+4)
11
>>> 
>>> print(ola mundo)
SyntaxError: invalid syntax
>>> '7'+'4'
'74'
>>> print('ola + 5)
      
SyntaxError: EOL while scanning string literal
>>> print('ola' + 5)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print('ola' + 5)
TypeError: can only concatenate str (not "int") to str
>>> print('Olá' , 5)
Olá 5
>>> nome='adriano'
>>> idade=36
>>> peso=90
>>> 
>>> print(nome,idade,peso)
adriano 36 90
>>> print(nome + idade + peso)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(nome + idade + peso)
TypeError: can only concatenate str (not "int") to str
>>> nome=imput('qual é o seu nome?')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    nome=imput('qual é o seu nome?')
NameError: name 'imput' is not defined
>>> nome = input ('Qual é o seu nome?')
Qual é o seu nome?Adriano
>>> idade = input ('Qual sua idade? ')
Qual sua idade? 36
>>> peso = input ('Qual o seu peso? ')
Qual o seu peso? 90.2
>>> print (nome , idade , peso)
Adriano 36 90.2
>>> 
=============================== RESTART: E:/User/Adriano/Desktop/Python/Screpts/teste01.py ==============================
Qual é o seu nome? Adriano
Qual a sua idade? 36
Qual o seu peso? 90,4
Adriano 36 90,4
>>> 