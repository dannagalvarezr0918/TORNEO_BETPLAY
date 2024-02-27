from tabulate import tabulate

from principal import principalofc
from modulos import equipo
from modulos import reportes
from modulos import fechas
import os

def menu_equipos():
    
    titulo = """
       +++++++++++++++++++++++++++
       +       MENU EQUIPO       +
       +++++++++++++++++++++++++++
"""
    os.system ('cls')
    print(titulo)

    menu = [["1.","Registrar Equipo"], ["2.","Menu principal"]]
    print(tabulate(menu,tablefmt="grid"))
    option = input()
    if option == '1':
        os.system('cls')
        equipo.agregar()
        menu_principal()
    else:
        os.system('cls')
        menu_principal()


def menu_principal():
     
    titulo = """
       ++++++++++++++++++++++++++++++++++
       +   LIGA BETPLAY COLOMBIA 2024   +
       ++++++++++++++++++++++++++++++++++
    """
    os.system ('cls')
    print(titulo)
    try:
        os.system('cls')
        menu = [["1.","Registrar equipo"],["2.","Registrar fecha de juego"], ["3.","Reportes"], ["4.","Salir"]]
        print(tabulate(menu,tablefmt="grid"))
        option = int(input("\n-"))
        if(option == 1):
            os.system('cls')
            menu_equipos()
        elif option == 2:
            os.system('cls')
            menu_fechas()
        elif option == 3:
            os.system('cls')
            menu_reportes()
        elif option == 4:
            os.system('cls')
            exit()
        else:
            menu_principal()
    except ValueError:
        menu_principal()

def menu_reportes():
    titulo = """
       ++++++++++++++++++++++++++++
       +       MENU REPORTES      +
       ++++++++++++++++++++++++++++
"""
    os.system ('cls')
    print(titulo)
    menu = [["A.","Nombre del equipo con más goles anotados"], ["B.","Nombre del equipo con más puntos"], ["C.","Nombre del equipo con más partidos ganados"], ["D.","Total de goles anotados por todos los equipos"], ["E.","Promedio de goles anotados en el torneo"], ["F.","Regresar al menú principal"]]
    print(tabulate(menu, tablefmt="grid"))

    option = input("\n-").upper()

    if len(principalofc) < 2:
        input("No hay suficientes equipos")
        menu_principal()

    if option == 'A':
        os.system('cls')
        reportes.top_goles_team()
        menu_principal()
    elif option == 'B':
        os.sysem('cls')
        reportes.top_puntos_team()
        menu_principal()
    elif option == 'C':
        os.system('cls')
        reportes.top_partidos_team()
        menu_principal()
    elif option == 'D':
        os.system('cls')
        reportes.goles_totales()
        menu_principal()
    elif option == "E":
        os.system('cls')
        reportes.promedio_goles()
        menu_principal()
    elif option == "F":
        menu_principal()
    elif option == "X":
        for equipo in principalofc:
            print(f"{equipo[0]}")
        input("Enter para volver")
        menu_reportes()
    else:
        os.system('cls')
        menu_reportes()

def menu_fechas():
  os.system('cls')
  
  titulo = """
       ++++++++++++++++++++++++++++
       +        MENU FECHAS       +
       ++++++++++++++++++++++++++++
"""
  os.system('cls')
  print(titulo)
  menu=[["1.","Agregar fecha"],["2.","Salir"]]
  print(tabulate(menu,tablefmt="grid"))
  option = input("\n-")

  if option == '1':
    if(len(principalofc) < 2):
        print("No hay suficientes equipos registrados, presiona ENTER")
        input()
    else:
        fechas.fecha()
    menu_principal()
  elif option == '2':
    return
  else:
    menu_fechas

