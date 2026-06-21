import conexaoBD


def Listar_Estoque():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Estoque")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult


def Atributos_Estoque():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SHOW COLUMNS FROM Estoque")
    atributos = mycursor.fetchall()
    mydb.close()

    colunas = []
    for n in range(len(atributos)):
        colunas.append(atributos[n][0])
    return colunas


def Cadastrar_Estoque(valores):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        colunas_lista = Atributos_Estoque()
        colunas_string = ",".join(colunas_lista)
        placeholders = ",".join(["%s"] * len(colunas_lista))

        sqlInsert = f"INSERT INTO Estoque ({colunas_string}) VALUES ({placeholders})"
        mycursor.execute(sqlInsert, tuple(valores))
        mydb.close()
        return True
    except:
        return False


def Update_Estoque(num_estoque, coluna, novo_valor):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        sqlUpdate = f"UPDATE Estoque SET {coluna} = %s WHERE Num_estoque = %s"
        mycursor.execute(sqlUpdate, (novo_valor, num_estoque))
        mydb.close()
        return True
    except:
        return False


def Delet_Estoque(num_estoque):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        sqlDelete = "DELETE FROM Estoque WHERE Num_estoque = %s"
        mycursor.execute(sqlDelete, (num_estoque,))
        mydb.close()
        return True
    except:
        return False
