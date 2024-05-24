import os
import tamagotchi
import threading
import time

# Función paso de tiempo y aumento de hambre, etc...
def paso_tiempo():
    while True:
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        mascota.nivel_hambre += 1
        mascota.nivel_energia -= 2
        mascota.nivel_felicidad -= 1
        print(f"Nombre de la mascota: {mascota.nombre}")
        mascota.verificar_estado()
        print("-----------------------")
    
        # Muestra las opciones al usuario
        print("Seleccione una opción:")
        print("1. Alimentar")
        print("2. Jugar")
        print("3. Dormir")
        print("4. Salir")

# Variable para verificar si el hilo ya ha sido iniciado
hilo_iniciado = False

# Limpia la consola
os.system('cls' if os.name == 'nt' else 'clear')

# Muestra el mensaje de bienvenida
print("Bienvenido al juego de Tamagotchi")
print("----------------------------------")
input("Presione Enter para comenzar...")
nombre = input("Ingrese el nombre para su mascota: ")

# Crea una instancia de la clase Tamagotchi
mascota = tamagotchi.Tamagotchi(nombre)

# Crea un hilo para el tiempo
hilo_aumentar_hambre = threading.Thread(target=paso_tiempo)

# Función para iniciar el hilo
def start_thread():
    global hilo_iniciado
    if not hilo_iniciado:
        hilo_aumentar_hambre.start()
        hilo_iniciado = True

# Inicia el hilo
start_thread()

# Bucle principal del juego
while True:
    # Limpia la consola
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Inicia el hilo
    start_thread()
    
    print(f"Nombre de la mascota: {mascota.nombre}")
    mascota.verificar_estado()
    print("-----------------------")
    
    # Muestra las opciones al usuario
    print("Seleccione una opción:")
    print("1. Alimentar")
    print("2. Jugar")
    print("3. Dormir")
    print("4. Salir")
    
    # Obtiene la opción seleccionada por el usuario
    opcion = input()
    
    # Realiza la acción seleccionada por el usuario
    if opcion == "1":
        mascota.alimentar()
    elif opcion == "2":
        mascota.jugar()
    elif opcion == "3":
        mascota.dormir()
    elif opcion == "4":
        hilo_aumentar_hambre.join()
        break
    else:
        print("Opción inválida")