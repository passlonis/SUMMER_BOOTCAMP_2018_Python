"""
self es el primer parametro que se pasa a cualquier metodo de clase.
Python usara el parametro self para referirse al objeto que se esta creando.
"""

class Complex:

    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

    def mostrar(self):
        return str(self.r) + "," + str(self.i)

numeroComplejo = Complex()
numeroComplejo.create(8, 9)
print(numeroComplejo.mostrar())

class Calculator:
    current = 7

    def add(self, amount):
       self.current += amount


    def get_current(self):
        return self.current

calculadora = Calculator()
calculadora.add(7)
print(calculadora.get_current())

# Para Complex cree el objeto y realize una llamada al metodo


# Para Calculator cree el objeto y realize llamadas a los metodos
# identifique y resuelva el problema
