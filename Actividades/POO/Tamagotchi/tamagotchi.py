import os
class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel_energia = 100  # Energía inicial en 100
        self.nivel_hambre = 0  # Hambre inicial en 0
        self.nivel_felicidad = 50  # Felicidad inicial en 50
        self.esta_vivo = True

    def mostrar_estado(self):
        print(f'Energia:{self.nivel_energia}\n Hambre:{self.nivel_hambre}\n Felicidad:{self.nivel_felicidad}')

    def verificar_estado(self):
        if self.nivel_energia <= 0:
            self.esta_vivo = False
            print(f'{self.nombre} ha muerto de cansancio')
            input('Presione Enter para cerrar el programa.')
            opcion = '4'
            os.system('cls' if os.name == 'nt' else 'clear')
        elif self.nivel_hambre >= 100:
            self.esta_vivo = False
            print(f'{self.nombre} ha muerto de hambre')
            input('Presione Enter para cerrar el programa.')
            opcion = '4'
            os.system('cls' if os.name == 'nt' else 'clear')
        elif self.nivel_felicidad <= 0:
            print(f'{self.nombre} ha muerto de tristeza')
            input('Presione Enter para cerrar el programa.')
            opcion = '4'
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            self.mostrar_estado()

    def alimentar(self):
        self.nivel_hambre = max(0, self.nivel_hambre - 10)  # Restringe el valor de hambre a un mínimo de 0
        self.nivel_energia = max(0, self.nivel_energia - 15)  # Restringe el valor de energía a un mínimo de 0
        print(f'{self.nombre} ha comido')

    def jugar(self):
        self.nivel_felicidad = min(100, self.nivel_felicidad + 20)  # Restringe el valor de felicidad a un máximo de 100
        self.nivel_energia = max(0, self.nivel_energia - 18)  # Restringe el valor de energía a un mínimo de 0
        self.nivel_hambre = min(100, self.nivel_hambre + 10)  # Restringe el valor de hambre a un máximo de 100
        print(f'{self.nombre} ha jugado')

    def dormir(self):
        self.nivel_energia = min(100, self.nivel_energia + 40)  # Restringe el valor de energía a un máximo de 100
        self.nivel_hambre = min(100, self.nivel_hambre + 5)  # Restringe el valor de hambre a un máximo de 100
        self.nivel_felicidad = max(0, self.nivel_felicidad - 10)  # Restringe el valor de felicidad a un mínimo de 0
        print(f'{self.nombre} ha dormido')


