"""
Un diccionario es similar a una lista, excepto que
tiene acceso a sus valores buscando una clave en lugar de un indice
"""
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

phone_book = {"John": 123, "Jane": 234, "Jerard": 345}
print(phone_book)


phone_book["Jill"] = 345
print(phone_book)


phone_book.pop("John")

print(phone_book["Jane"])

print("-------------------------------------------------")

agenda = {"marco": 1111, "jc": 2222, "ariel": 3333, "jorge": 4444, "maria": 5555}
print(agenda)

agenda["morena"] = 6666
print(agenda)

print(agenda["ariel"])

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")