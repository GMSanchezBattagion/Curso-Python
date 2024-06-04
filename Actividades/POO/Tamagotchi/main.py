import os
import tamagotchi
import threading
import time
opcion = ""
# Función para el paso del tiempo y aumento de hambre, etc.
def paso_tiempo():
    while True:
        global opcion
        if opcion == "4": break
        else:
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            mascota.nivel_hambre += 1
            mascota.nivel_energia -= 2
            mascota.nivel_felicidad -= 1
            print(f"Nombre de la mascota: {mascota.nombre}")
            mascota.verificar_estado()
            print("-----------------------")

            # Mostrar opciones al usuario
            print("Seleccione una opción:")
            print("1. Alimentar")
            print("2. Jugar")
            print("3. Dormir")
            print("4. Salir")

# Variable para verificar si el hilo ya ha sido iniciado
hilo_iniciado = False

# Limpiar la consola
os.system('cls' if os.name == 'nt' else 'clear')

# Mostrar mensaje de bienvenida
print("Bienvenido al juego de Tamagotchi")
print("----------------------------------")
input("Presione Enter para comenzar...")
nombre = input("Ingrese el nombre para su mascota: ")

# Crear una instancia de la clase Tamagotchi
mascota = tamagotchi.Tamagotchi(nombre)

# Crear un hilo para el tiempo
hilo_aumentar_hambre = threading.Thread(target=paso_tiempo)

# Función para iniciar el hilo
def start_thread():
    global hilo_iniciado
    if not hilo_iniciado:
        hilo_aumentar_hambre.start()
        hilo_iniciado = True

# Iniciar el hilo

start_thread()
# Bucle principal del juego
while True:
    # Limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"Nombre de la mascota: {mascota.nombre}")
    mascota.verificar_estado()
    print("-----------------------")
    
    # Mostrar opciones al usuario
    print("Seleccione una opción:")
    print("1. Alimentar")
    print("2. Jugar")
    print("3. Dormir")
    print("4. Salir")
    
    # Obtener la opción seleccionada por el usuario
    opcion = input()
    
    # Realizar la acción seleccionada por el usuario
    if opcion == "1":
        mascota.alimentar()
    elif opcion == "2":
        mascota.jugar()
    elif opcion == "3":
        mascota.dormir()
    elif opcion == "4":
        # Salir del juego cuando se selecciona la opción 4
        hilo_aumentar_hambre.join()
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        print("Opción inválida")
hilo_aumentar_hambre.join()
os.system('cls' if os.name == 'nt' else 'clear')
