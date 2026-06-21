import conexaoBD


def Listar_Marca():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Marca")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult


def Atributos_Marca():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SHOW COLUMNS FROM Marca")
    atributos = mycursor.fetchall()
    mydb.close()

    colunas = []
    for n in range(len(atributos)):
        colunas.append(atributos[n][0])
    return colunas


def Cadastrar_Marca(valores):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        colunas_lista = Atributos_Marca()
        colunas_string = ",".join(colunas_lista)
        placeholders = ",".join(["%s"] * len(colunas_lista))

        sqlInsert = f"INSERT INTO Marca ({colunas_string}) VALUES ({placeholders})"
        mycursor.execute(sqlInsert, tuple(valores))
        mydb.close()
        return True
    except:
        return False


def Update_Marca(cnpj, coluna, novo_valor):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        sqlUpdate = f"UPDATE Marca SET {coluna} = %s WHERE CNPJ = %s"
        mycursor.execute(sqlUpdate, (novo_valor, cnpj))
        mydb.close()
        return True
    except:
        return False


def Delet_Marca(cnpj):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        sqlDelete = "DELETE FROM Marca WHERE CNPJ = %s"
        mycursor.execute(sqlDelete, (cnpj,))
        mydb.close()
        return True
    except:
        return False
