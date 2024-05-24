import time
import os
class Tamagotchi:
    nivel_energia=100   
    nivel_hambre=0
    nivel_felicidad=50
    esta_vivo=True
    def __init__(self, nombre):
        self.nombre=nombre
        
    
    def mostrar_estado(self):
        print(f'Energia:{self.nivel_energia}\n Hambre:{self.nivel_hambre}\n Felicidad:{self.nivel_felicidad}')
    
    def verificar_estado(self):
        if self.nivel_energia <= 0:
            self.esta_vivo = False
            print(f'{self.nombre} ha muerto de cansancio')
        elif self.nivel_hambre >= 100:
            self.esta_vivo = False
            print(f'{self.nombre} ha muerto de hambre')
        elif self.nivel_felicidad<=0:
            print(f'{self.nombre} ha muerto de tristeza')
        else:
            self.mostrar_estado()
        
    def alimentar(self):
        self.nivel_hambre-=10
        self.nivel_energia-=15
        print(f'{self.nombre} ha comido')
    
    def jugar(self):
        self.nivel_felicidad+=20
        self.nivel_energia-=18
        self.nivel_hambre+=10
        print(f'{self.nombre} ha jugado')
    
    def dormir(self):
        self.nivel_energia+=40
        self.nivel_hambre+=5
        self.nivel_felicidad-=10
        print(f'{self.nombre} ha dormido')


