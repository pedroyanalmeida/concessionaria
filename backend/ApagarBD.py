import conexaoBD

# CUIDADO: este arquivo APAGA o banco inteiro!
# Só rode se quiser zerar tudo e recriar do zero.
mydb = conexaoBD.conectar()
mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE IF EXISTS agenciacarros")
