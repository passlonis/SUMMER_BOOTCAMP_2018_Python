print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

count = 0

while True:
    print(count)
    count += 1
    if count == 5:
        break


zoo = ["lion", 'tiger', 'elephant']
while True:
    animal = zoo.pop()
    print(animal)
    if animal is 'tiger':
        break

print("--------------------------------------------------------")

contador = 0
while(True):
    contador+=1
    print(contador)
    if(contador == 10):
        break


nombres = ["luz", "maria", "jose", "perla"]
while(len(nombres) < len(nombres)+1):
    n = nombres.pop()#elimina el ultimo valor de la lista nombres
    print(n)
    if(n == "perla"):
        break

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")