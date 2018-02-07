"""
los loops se utilizan para iterar sobre una secuencia dada.
En cada iteracion, la variable definida en el ciclo for se asignara
al siguiente valor en la lista.
El tipo de range representa una secuencia de numeros inmutable
https://docs.python.org/3/library/stdtypes.html#typesseq-range
"""
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

for i in range(5):    # range(5) retorna 0, 1, 2, 3, 4
    print(i)

primes = [2, 3, 5, 7]

for prime in primes:
    print(prime)

print("-----------------------------------------------------")

for j in range(10):
    print(j)

pares = [0, 2, 4, 6, 8, 10]
for par in pares:
    print(par)

print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
