from tabulate import tabulate
import os

from principal import  principalofc, lookinge

def fecha():
  os.system('cls')
  
  titulo = """
       ++++++++++++++++++++++++++++
       +        MENU FECHAS       +
       ++++++++++++++++++++++++++++
"""
  os.system('cls')
  print(titulo)


  print(tabulate(principalofc, headers="keys",tablefmt="grid"))
  equipo_local = input("Nombre del equipo local\n ").capitalize()
  local = lookinge(equipo_local)
  if not(local):
    print("Equipo inexistente")
    input("Enter para volver al menu principal")
    return

  equipo_visitante = input("Nombre del equipo visitante ").capitalize()
  visitante = lookinge(equipo_visitante)
  if not(visitante):
    print("Equipo inexistente")
    input("Enter para volver al menu principal")
  

    os.system('cls')
    print(titulo)

    goles_local = int(input(f"Goles anotad {local}: "))
    goles_visitante = int(input(f"Goles anotados {visitante}: "))

    local["PJ"] += 1
    local["GF"] += goles_local
    local["GC"] += goles_visitante

    visitante["PJ"] += 1
    visitante["GF"] += goles_visitante
    visitante["GC"] += goles_local

  if goles_local > goles_visitante:
    local["TP"] += 3
    local["PG"] += 1
    visitante["PP"] += 1
  elif goles_visitante > goles_local:
    visitante["TP"] += 3
    visitante["PG"] += 1
    local["PP"] += 1
  else:
    local["TP"] += 1
    local["PE"] += 1
    visitante["TP"] += 1
    visitante["PE"] += 1

  print(tabulate([local, visitante], headers="keys", tablefmt="grid"))
  input("Presiona enter para volver al menú principal")
  return




  