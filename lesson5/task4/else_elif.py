"""
La instruccion else complementa la instruccion if.
La palabra clave elif es la abreviatura de "else if".
"""
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

x = 28

if x < 0:
    print('x < 0')
elif x == 0:
    print('x is zero')
elif x == 1:
    print('x == 1')
else:
    print('Ninguno fue True')

name = "John"

if name == 'John':
    print(True)
else:
    print(False)

print("-----------------------------------------------------")

x = 0
if(x<0):
    print("x es menos a 0")
else:
    if(x==0):
        print("x tiene el valor de 0")
    else:
        if(x==1):
            print("x es igual a 1")

        else: print("niguno es verdadero")


nombre = "ariel"
if(nombre == "Ariel"):
    print(True)

else:
    print(False)


print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
