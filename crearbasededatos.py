import MySQLdb
import mysql.connector
import os

server = MySQLdb.connect(
  host = "localhost",
  user = "root",
  passwd = "direla")

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="direla"
)

salir = False


while salir == False:
  print("Que quieres (V)er, (C)rear ,(B)orrar? o (S)alir: ")
  pregunta = input()

  if pregunta == 'Crear' or pregunta == 'C':
    print("Inserta el nombre de la nueva base de datos")
    nombreBDD = input()
    cursorObject = dataBase.cursor()
    cursorObject.execute('CREATE DATABASE %s' %nombreBDD)

  elif pregunta == 'Borrar' or pregunta == 'B':

    cur = dataBase.cursor()
    curServ = server.cursor()
    databases = ("show databases")
    cur.execute(databases)
    for (databases) in cur:
      print("·", databases[0])
    
    print('Escribe la base de datos que quieres borrar: ')
    nombreBDD = input()
    cursorObject = dataBase.cursor()
    cursorObject.execute('DROP DATABASE %s;' %nombreBDD)

  elif pregunta == 'Ver' or pregunta == 'V':

    cur = dataBase.cursor()
    curServ = server.cursor()

    databases = ("show databases")
    cur.execute(databases)
    for (databases) in cur:
      print("·", databases[0])
  
  elif pregunta == 'Salir' or pregunta == 'S':
    os.system("clear")
    print("Cleared and Exited :)")
    salir = True

  else:
    print("Escribe una respuesta correcta!")
    os.system("sudo python3 crearbasededatos.py")