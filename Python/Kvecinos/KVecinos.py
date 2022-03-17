#Contiene los datos y servicios relacionados con el control de usuarios 
import hashlib
from math import sqrt 

class Persona:
    def __init__(self, nombre, valoraciones):
        self.nombre = nombre
        self.valoraciones = valoraciones
        indice = hashlib.sha256()
        nombreCod = bytes(nombre, 'utf-8')
        indice.update(nombreCod)
        self.id = indice.hexdigest()

    def __str__(self):
        salida = "Id: " + self.id + "\nNombre: " + self.nombre + "\nValoraciones: " + str(self.valoraciones)
        return salida

    def setValoraciones(self, valoraciones):
        self.valoraciones = valoraciones.copy()

    def setNombre(self, nombre):
        self.nombre = nombre

    def getValoraciones(self):
        return self.valoraciones

    def getNombre(self):
        return self.nombre

    #Metodos funcionales

    def calcularNorma(self):
        suma = 0
        for valor in self.valoraciones:
            suma += valor * valor
        return sqrt(suma)
    
    def calcularSumaCuadrados(self):
        suma = 0
        for valor in self.valoraciones:
            suma += valor * valor
        return suma
    
    def calcularCuadradoSuma(self):
        suma = 0 
        for valor in self.valoraciones:
            suma += valor
        return suma * suma

    def calcularSumatoria(self):
        suma = 0
        for valor in self.valoraciones:
            suma += valor
        return suma

juan = Persona("Juan Cristomo Santos Putin", [3,3.5,7,8,9])

print(juan)
print(juan.calcularNorma())