import json
class Personaje:
    def __init__(self, nombre, clase, raza, nivel):
        self.nombre = nombre
        self.clase = clase
        self.raza = raza
        self.nivel = nivel
        
        with open('vpj.json', "r") as file:
            datos_clases = json.load(file)
        with open('razas.json', "r") as file:
            datos_razas = json.load(file)
        with open('eq.json', "r") as file:
            datos_eq = json.load(file)
        self.fuerza = datos_clases["Clases"][clase]["Caracteristicas"]["Fuerza"] + datos_razas["Razas"][raza]["Car_ad"]["Fuerza"]
        self.destreza = datos_clases["Clases"][clase]["Caracteristicas"]["Destreza"] + datos_razas["Razas"][raza]["Car_ad"]["Destreza"]
        self.constitucion = datos_clases["Clases"][clase]["Caracteristicas"]["Constitucion"] + datos_razas["Razas"][raza]["Car_ad"]["Constitucion"]
        self.inteligencia = datos_clases["Clases"][clase]["Caracteristicas"]["Inteligencia"] + datos_razas["Razas"][raza]["Car_ad"]["Inteligencia"]
        self.sabiduria = datos_clases["Clases"][clase]["Caracteristicas"]["Sabiduria"] + datos_razas["Razas"][raza]["Car_ad"]["Sabiduria"]
        self.carisma = datos_clases["Clases"][clase]["Caracteristicas"]["Carisma"] + datos_razas["Razas"][raza]["Car_ad"]["Carisma"] 
        self.vida_maxima = datos_clases["Clases"][clase]["HP"] * self.nivel + datos_eq["Valores"][str(self.constitucion)]
        
