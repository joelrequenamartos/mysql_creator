import mysql.connector

def insert_varibles_into_table(NAME,SURNAME, AGE):

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Pruebas',
                                             user='root',
                                             password='direla')

        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Pruebas (NAME, SURNAME, AGE) 
                                VALUES (%s, %s, %s) """

        record = (NAME, SURNAME, AGE)
        cursor.execute(mySql_insert_query, record)
        connection.commit()

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
print("Name: ")
variable1 = input()
print("Surname: ")
variable2 = input()
print("Age: ")
variable3 = input()


insert_varibles_into_table(variable1, variable2, variable3)