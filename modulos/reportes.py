from principal import principalofc
import os

def winnerofc(categoria, mensaje,):
   
    titulo = """
       +++++++++++++++++++++++++++++
       +       MENU REPORTES       +
       +++++++++++++++++++++++++++++
"""
    os.system ('cls')
    print(titulo)
    winner = ""
    puntos = 0
    for equipo in principalofc:
     if equipo[categoria] > puntos:
      puntos = equipo[categoria]
      winner = equipo["Nombre"]
      print(f"El equipo ganador fue: {winner} con {puntos} {mensaje}")
      input("Enter para volver a la pantalla principal")
os.system ('cls')

def top_goles_team():
  winnerofc("GF", "goles")

def top_puntos_team():
  winnerofc("TP", "puntos")

def top_partidos_team():
  winnerofc("PG", "partidos")

def goles_totales():
  goles = 0
  for equipo in principalofc:
    goles += equipo["GF"]
  print(f"Se anotaron {goles} goles en el campeonato")
  input("Enter para volver a la pantalla principal")
  os.system ('cls')

def promedio_goles():
  goles = 0
  for equipo in principalofc:
    goles += equipo["GF"]
  promedio = goles / len(principalofc)
  print(f"Se anotaron en promedio {promedio} en el campeonato")
  input("Enter para volver a la pantalla principal")
  os.system ('cls')
