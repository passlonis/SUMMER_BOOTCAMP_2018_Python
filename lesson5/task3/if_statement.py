"""
La palabra reservada if se usa para formar una instruccion condicional
que ejecuta algun codigo
especificado despues de verificar si su expresion es True.
Python usa indentacion para definir bloques de codigo.
"""

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

name = "John"
age = 17

if name == "John" or age == 17:
    print("name is John")
    print("John is 17 years old")

tasks = ['task1', 'task2']

if len(tasks) == 0:
    print("empty")

print("------------------------------------------------------")

nombre = "ariel"
edad = 28

if(nombre == "ariel" and edad == 28):
    print("hola soy ariel y tengo 28 anios")

lista = [1, 2, 3, 4, 5]
if(not len(lista) == 0):
    print("La lista no esta vacia")

lista = []
if(len(lista)==0):
    print("La lista esta vacia")



print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
