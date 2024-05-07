import random

def repeat():
    while True:
        opciones=["piedra","papel","tijera"]
        pptr=random.choice(opciones)
        eleccion=input("Elije Piedra, Papel o Tijeras  ")
        
        if eleccion.lower() == "piedra":
            if pptr == "tijera":        
                print(f"Elejiste " + eleccion + " y la computadora eligio " + pptr + ", has ganado")
            elif pptr == "piedra":
                print(f"Elejiste " + eleccion + " y la computadora eligio " + pptr + ", es un empate")
            else:        
                print(f"Elejiste " + eleccion + " y la computadora eligio " + pptr + ", has perdido")
            
        elif eleccion.lower() == "papel":
            if pptr == "tijera":        
                print(f"Elejiste " + eleccion + " y la computadora eligio " + pptr + ", has perdido")
            elif pptr == "papel":
                print(f"Elejiste " + eleccion + " y la computadora eligio " + pptr + ", es un empate")                   
            elif pptr == "piedra":     
                print(f"Elejiste " + eleccion + " y la computadora eligio " + pptr + ", has ganado")
        
        elif eleccion.lower() == "tijera" or eleccion.lower() == "tijeras":
            if pptr == "papel":        
                print(f"Elejiste " + eleccion + " y la computadora eligio " + pptr + ", has ganado")
            elif pptr == "tijera":
                print(f"Elejiste " + eleccion + " y la computadora eligio " + pptr + ", es un empate")
            else:       
                print(f"Elejiste " + eleccion + " y la computadora eligio " + pptr + ", has perdido")
        else:
            print("Opción inválida")

        continuar = input("¿Quieres seguir jugando? (s/n): ")
        if continuar.lower() != "s":
            break
repeat()
