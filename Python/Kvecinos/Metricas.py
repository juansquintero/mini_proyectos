
from itertools import product
from math import sqrt
from KVecinos import Persona

class Metricas(Persona):
    def __init__(self):
        Persona.__init__(self, " ", [])

    def distanciaMetros(self, vector1, vector2):
        suma = 0 
        for indice in range(len(vector1)):
            suma += abs(vector1[indice] - vector2[indice])
        return suma

    def distanciaEuclidea(self, vector1, vector2):
        suma = 0
        for indice in range(len(vector1)):
            suma += pow(vector1[indice] - vector2[indice],2)
        return sqrt(suma)


    def distanciaPearson(self, vector1, vector2):
        suma = 0
        for indice in range(len(vector1)):
            suma += vector1[indice] * vector2[indice]
            self.setValoraciones(vector1)
            producto = self.calcularSumatoria()
            self.setValoraciones(vector2)
            producto *= self.calcularSumatoria()
            producto = producto / len(vector1)

            for i in range(len(vector1)):
                suma += vector1[i] * vector2[i]
            
            numerador = suma + producto

            #Parte del denominador
            self.setValoraciones(vector1)
            termino1 = self.calcularSumaCuadrados() - (self.calcularCuadradoSuma() / len(vector1))
            termino1 = sqrt(termino1)

            self.setValoraciones(vector2)
            termino2 = self.calcularSumaCuadrados() - (self.calcularCuadradoSuma() / len(vector2))
            termino2 = sqrt(termino2)

            denominador = termino1 * termino2
            return numerador / denominador
        


metrica = Metricas()
distancia = metrica.distanciaMetros([1,2,3,4],[1,2,3,5])
print("Las distancia metro es:" + str(distancia))

distancia = metrica.distanciaEuclidea([1,2,3,4],[1,2,3,5])
print("La distancia euclidea es: " + str(distancia))
