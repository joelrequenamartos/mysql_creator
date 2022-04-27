import diccionario
import os

diccionario.importarconexiones()
salir = False

while salir == False:
  print("Que quieres (V)er, (C)rear ,(B)orrar? o (S)alir: ")
  pregunta = input()

  if pregunta == 'Crear' or pregunta == 'C':
    diccionario.crearbdd()

  elif pregunta == 'Borrar' or pregunta == 'B':
    diccionario.showdatabase()
    diccionario.borrarbdd()

  elif pregunta == 'Ver' or pregunta == 'V':
    diccionario.showdatabase()
  
  elif pregunta == 'Salir' or pregunta == 'S':
    os.system("clear")
    salir = True
    print("Cleared and Exited :)")

  else:
    os.system("clear")
    print("Escribe una respuesta correcta!")