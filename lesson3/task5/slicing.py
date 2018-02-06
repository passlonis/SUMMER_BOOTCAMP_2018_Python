"""
Slicing se usa para obtener varios caracteres (una subcadena) de una cadena.
Su sintaxis es similar a la de indexacion, pero en lugar de solo un indice,
utiliza dos indices (numeros) separados por dos puntos
Ej. str[ind1:ind2]

str[inicio:fin] # elementos comienzan hasta el final-1
str[inicio:]    # elementos comienzan por el resto de la matriz
str[: end]      # elementos desde el principio hasta el final-1
str[:]          # una copia completa

"""
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

monty_python = "Monty_Python"
monty = monty_python[:4]      # one or both index could be dropped. monty_python[:5] is equal to monty_python[0:5]
print(monty)
python = monty_python[6:11] # (P-6)(n-11) Python
print(python)

print("------------------------------------------------------")

cadena = "Aprendiendo a programar en PYTHON"
print(cadena[0:33]) #imprime todo
print(cadena[27:]) #imprime PYTHON
print(cadena[:33]) #imprime todo
print(cadena[:]) #imprime todo
print(cadena[:11]) #imprime aprendiendo

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")



