"""
Los operadores booleanos comparan declaraciones y devuelven resultados
en valores booleanos.
El operador booleano "and".
El operador booleano "or".
El operador booleano not invierte la expresion booleana.
"""
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

name = "John"
age = 17

print(name == "John" or age == 17)

# Si el nombre es igual a "John" y no tiene 23 anios.
print(name == "John" and not (age==23))

print("----------------------------------------------------")

nombre = "ariel"
edad = 28

print(nombre == "ariel" and edad == 28)
print(nombre == "Ariel" and not edad == 27)

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
