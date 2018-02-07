print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
class Car:
    color = ""
    def description(self):
        description_string = "This is a %s car." % self.color
        return description_string

car1 = Car()
car2 = Car()

car1.color = "blue"
car2.color = "red"

print(car1.description())
print(car2.description())

print("------------------------------------------------------------------------")

class Auto:
    colorAuto = ""
    def caracteriticas(self):
        descripcion = " el auto es de color " + self.colorAuto
        return descripcion

auto1 = Auto()
auto2 = Auto()

auto1.colorAuto = "rojo"
auto2.colorAuto = "verde"

print(auto1.caracteriticas())
print(auto2.caracteriticas())

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")