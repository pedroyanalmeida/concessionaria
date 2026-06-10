import conexaoBD

mydb = conexaoBD.conectar()
mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE IF EXISTS agenciacarros")