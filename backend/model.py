import conexaoBD


def Listar_Modelo():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Modelo")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult


def Atributos_Modelo():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SHOW COLUMNS FROM Modelo")
    atributos = mycursor.fetchall()
    mydb.close()

    colunas = []
    for n in range(len(atributos)):
        colunas.append(atributos[n][0])
    return colunas


def Cadastrar_Modelo(valores):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        colunas_lista = Atributos_Modelo()
        colunas_string = ",".join(colunas_lista)
        placeholders = ",".join(["%s"] * len(colunas_lista))

        sqlInsert = f"INSERT INTO Modelo ({colunas_string}) VALUES ({placeholders})"
        mycursor.execute(sqlInsert, tuple(valores))
        mydb.close()
        return True
    except:
        return False


def Update_Modelo(id_modelo, coluna, novo_valor):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        sqlUpdate = f"UPDATE Modelo SET {coluna} = %s WHERE idModelo = %s"
        mycursor.execute(sqlUpdate, (novo_valor, id_modelo))
        mydb.close()
        return True
    except:
        return False


def Delet_Modelo(id_modelo):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        sqlDelete = "DELETE FROM Modelo WHERE idModelo = %s"
        mycursor.execute(sqlDelete, (id_modelo,))
        mydb.close()
        return True
    except:
        return False
