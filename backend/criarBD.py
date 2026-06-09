import mysql.connector


def criar():
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="$Xilipefe123",
        )

        mycurso = mydb.cursor()
        mycurso.execute("CREATE DATABASE IF NOT EXISTS agenciacarros")
    except:
        print("Erro ao criar o banco")
        return 0