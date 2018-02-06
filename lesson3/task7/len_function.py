"""
La funcion len() se usa para contar cuantos caracteres contiene una cadena.
obtener la primera mitad de la frase
"""
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
first_half = phrase[:int(len(phrase)/2)]
print(first_half)

print("--------------------------------------------------")

cadena = "esta es una cadena muy pero muy larga"
print(len(cadena))
print(cadena[0:int(len(cadena)/2)])

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

