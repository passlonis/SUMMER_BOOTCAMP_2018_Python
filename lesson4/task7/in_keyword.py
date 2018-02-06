"""
La palabra clave "in" se usa para verificar si una lista o un diccionario
contiene un elemento especifico.
Se puede aplicar a listas o diccionarios
de la misma manera que se hizo con las cadenas.
"""
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

grocery_list = ["fish", "tomato", 'apples']

print("tomato" in grocery_list)

grocery_dict = {"fish": 1, "tomato": 6, 'apples': 3}

print('fish' in grocery_dict)

print("----------------------------------------------------")

lista_laptops = ["mac", "lenovo", "dell", "vaio", "toshiba"]
print("mac" in lista_laptops)

lista_laptops_importancia = {"mac": 1, "lenovo": 2, "dell": 3, "vaio": 4, "toshiba": 5}
print("dell" in lista_laptops_importancia)
print("akita" in lista_laptops_importancia)

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
