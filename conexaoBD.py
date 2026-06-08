import mysql.connector
import criarBD

def conectar():
    try:
        criarBD.criar()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="$Xilipefe123",
        database="agenciacarros"
        )
        return mydb
    except:
        print("Erro de conecatar o banco")