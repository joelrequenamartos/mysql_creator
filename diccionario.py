import MySQLdb
import mysql.connector
server = MySQLdb.connect(
  host = "localhost",
  user = "root",
  passwd = "direla")
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="direla"
)


def importarconexiones():
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

def showdatabase():
    cur = dataBase.cursor()
    curServ = server.cursor()
    
    databases = ("show databases")
    cur.execute(databases)
    for (databases) in cur:
      print("·", databases[0])

def crearbdd():
    print("Inserta el nombre de la nueva base de datos")
    nombreBDD = input()
    cursorObject = dataBase.cursor()
    cursorObject.execute('CREATE DATABASE %s' %nombreBDD)

def borrarbdd():
    print('Escribe la base de datos que quieres borrar: ')
    nombreBDD = input()
    cursorObject = dataBase.cursor()
    cursorObject.execute('DROP DATABASE %s;' %nombreBDD)