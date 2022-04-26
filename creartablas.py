
# importing required libraries
import mysql.connector

 
def creartabla():

  dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="direla",
    database = "PruebaCreacion"
  )

  cursorObject = dataBase.cursor()
  nameInfo = """CREATE TABLE Pruebas (
                    NAME  VARCHAR(20) NOT NULL,
                    SURNAME VARCHAR(20),
                    AGE INT
                    )"""
    

  cursorObject.execute(nameInfo)
    
  dataBase.close()

