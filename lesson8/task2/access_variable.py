"""
Puede cambiar los valores de las variables definidas en una clase
para diferentes instancias(objetos) de esta clase.
"""
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.")
class MyClass:
    variable1 = 45
    variable2 = 180

    def foo(self):
        print("Hello from function foo")

my_object = MyClass()
my_object1 = MyClass()

my_object.variable2 = 3

print(my_object.variable2)
print(my_object1.variable2)

my_object.foo()

print(my_object.variable1)


print("-----------------------------------------------------------------------")

class MiClase:
    numero1 = 5
    numero2 = 10

    def impresion(self):
        for i in range(2):
            print("hola")


miclase1 = MiClase()
print(str(miclase1.numero1) + "----" + str(miclase1.numero2))
miclase1.impresion()

miclase2 = MiClase()
miclase2.numero1 = 4
miclase2.numero2 = 8
print(str(miclase2.numero1) + "----" + str(miclase2.numero2))
miclase2.impresion()

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.")

