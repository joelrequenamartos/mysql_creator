import MySQLdb
import mysql.connector
import os

salir = False
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

def selectDatabase():
    inputdatabase = input()
    dataBase = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="direla"
        database = inputdatabase
    )

    cursor = dataBase.cursor()

def insertdatabase():
    print("Quieres insertar datos en alguna BBD?: ")
    print("(S)i, (N)o")
    
    if insertardatos == 'Si' or insertardatos == 'S':
        print("Que base de datos quieres usar?: ")
        showdatabase()
    insertardatos = input()

    if insertardatos == 'No' or insertardatos == 'N':
        os.system("exit")

def crearbdd():
    print("Inserta el nombre de la nueva base de datos")
    nombreBDD = input()
    cursorObject = dataBase.cursor()
    cursorObject.execute('CREATE DATABASE %s' %nombreBDD)

    selectDatabase()

def borrarbdd():
    print('Escribe la base de datos que quieres borrar: ')
    nombreBDD = input()
    cursorObject = dataBase.cursor()
    cursorObject.execute('DROP DATABASE %s;' %nombreBDD)