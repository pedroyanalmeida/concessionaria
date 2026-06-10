import mysql.connector
import criarBD

def conectar():
    try:
        criarBD.criar()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="agenciacarros"
        )
        mydb.autocommit = True
        return mydb
    except:
        print("Erro em conectar ao banco")