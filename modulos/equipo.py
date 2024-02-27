from principal import principalofc
import os

def agregar():
    titulo = """
       +++++++++++++++++++++++++++
       +       MENU EQUIPO       +
       +++++++++++++++++++++++++++
"""
    os.system ('cls')
    print(titulo)
    nombre_equipo = input("Escriba el nombre del equipo ").capitalize()
    
    equipo = {
            "Nombre": nombre_equipo,
            "PJ": 0,
            "PG": 0,
            "PP": 0,
            "GF": 0,
            "GC": 0,
            "TP": 0,
            }
    principalofc.append(equipo)
    print(principalofc)
    input("Enter para continuar")
    os.system('cls')