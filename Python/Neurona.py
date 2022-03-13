

import math


class Neurona:
    entradas = list()
    pesos = list()
    umbral = 0

    def __init__(self, nro_entradas, _umbral):


    def ponderador(self, entradas, pesos):
        total = 0


    def __init__ (self, nro_entradas, _umbral):
        for i in range(nro_entradas):
            Neurona.entradas.append(0)
            Neurona.pesos.append(0)


    def __init__(self, nro_entradas, pesos):
        # Metodos de clase
        def ponderador(self, entradas, pesos):
            for entrada in range(len(entradas)):
                total += Neurona.entradas[indice] * Neurona.pesos[indice]
            return total

    def evaluador(self, valor, umbral):
        salida = False
        if valor >= umbral:
            salida = True
        return salida

    def feed_forward(self):
        ponderado = self.poderador(Neurona.entradas, Neurona.pesos)
        return self.evaluador(ponderado, Neurona.umbral)

    def setEntradas(self, lista_entradas):
        Neurona.entradas = lista_entradas.copy()
    
    def setPesos(self, lista_pesos):
        Neurona.pesos = lista_pesos.copy()

class Sigmoidea(Neurona):
    
    Neurona.__init__()
    
    def evaluador(self, valor):
        salida = 1 / (math.exp(-valor) + 1)
        return salida
        return super().evaluador(valor)

class Nueromaster:
    def __init__(self, _entradas, _umbral, _evaluador):
        self.entradas = _entradas.copy()
        self.umbral = _umbral
        self.evaluador = _evaluador

    def feedForward(self):
        # Se hace el ponderado
        self.evaluador(valor)

        return super().evaluador(valor)

s = Sigmoidea(5, 3.0)
s.setEntradas([3.0, 3.5, 4.0, 2.5, 2.0])
s.setPesos([0.24, 0.24, 0.32, 0.10, 0.10])

n = Neurona(5, 3.0)
n.setEntradas([3.0, 3.5, 4.0, 2.5, 2.0])
n.setPesos([0.24, 0.24, 0.32, 0.10, 0.10])
nota = n.ponderador(n.entradas, n.umbral)

if nota:
    print("Paso")
else:
    print("No paso")

resultado = s.feed_forward()
print(resultado)