
import random as rd

class Dados:
    def __init__(self, caras):
        self.caras = caras
    def tirar(self):
        return rd.randint(1, self.caras)




