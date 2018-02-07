print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

for i in range(5):
    if i == 3:
        continue
    print(i)

print("======")
for x in range(10):
    if x%2==0:
        continue
    print(x)

print("--------------------------------------------------------------")

pares = 0
for pares in range(20):
    if pares == 1  or pares == 3 or pares == 5 or pares == 7 or pares == 9 or pares == 11 or pares == 13 or pares == 15 or pares == 17 or pares == 19:
        pares += 1
        continue
    print(pares)


impares = 0
for impares in range(20):
    if impares%2 == 0:
        continue
    print(impares)

print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")