import conexaoBD


def Listar_Venda():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Venda")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult


def Atributos_Venda():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SHOW COLUMNS FROM Venda")
    atributos = mycursor.fetchall()
    mydb.close()

    colunas = []
    for n in range(len(atributos)):
        colunas.append(atributos[n][0])
    return colunas


def Cadastrar_Venda(valores):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        colunas_lista = Atributos_Venda()
        colunas_string = ",".join(colunas_lista)
        placeholders = ",".join(["%s"] * len(colunas_lista))

        sqlInsert = f"INSERT INTO Venda ({colunas_string}) VALUES ({placeholders})"
        mycursor.execute(sqlInsert, tuple(valores))
        mydb.close()
        return True
    except:
        return False


def Update_Venda(num_venda, coluna, novo_valor):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        sqlUpdate = f"UPDATE Venda SET {coluna} = %s WHERE Num_venda = %s"
        mycursor.execute(sqlUpdate, (novo_valor, num_venda))
        mydb.close()
        return True
    except:
        return False


def Delet_Venda(num_venda):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        sqlDelete = "DELETE FROM Venda WHERE Num_venda = %s"
        mycursor.execute(sqlDelete, (num_venda,))
        mydb.close()
        return True
    except:
        return False
