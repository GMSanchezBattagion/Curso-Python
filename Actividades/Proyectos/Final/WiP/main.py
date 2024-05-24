import json
import random
import dados
import personaje


with open('vpj.json', "r") as file:
    datos_clases = json.load(file)
with open('razas.json', "r") as file:
    datos_razas = json.load(file)
with open('eq.json', "r") as file:
    datos_eq = json.load(file)
    
    
dados.tirar(20)
