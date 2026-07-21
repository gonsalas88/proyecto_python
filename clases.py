class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, soy", self.nombre, "y tengo", self.edad, "años")


persona1 = Persona("Erick", 22)
persona1.saludar()
