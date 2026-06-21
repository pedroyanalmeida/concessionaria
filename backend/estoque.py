import conexaoBD

def Listar_Estoque():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Estoque")
    myresult = mycursor.fetchall()
    mydb.close()
    
    return myresult

def Printar_Estoque():
    estoques = Listar_Estoque()
    for n in range(len(estoques)):
        print(f"{n+1}- {estoques[n]}")

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

def Printar_Atributos():
    estoques = Atributos_Estoque()
    for n in range(len(estoques)):
        print(f"{n+1}- {estoques[n]}")

def Cadastrar_Estoque(valores): 
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        colunas_lista = Atributos_Estoque()
        colunas_string = ",".join(colunas_lista)
        
        placeholders = ",".join(["%s"] * len(colunas_lista))

        sqlInsert = f"INSERT INTO Estoque ({colunas_string}) VALUES ({placeholders})"

        mycursor.execute(sqlInsert, valores)
        mydb.close()
 
        return True
    except:
        return False

def Update_Estoque(estoqueID, coluna, novo_valor):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
                
        num_estoque = estoqueID

        sqlUpdate = f"UPDATE Estoque SET {coluna} = %s WHERE Num_estoque = %s"
        mycursor.execute(sqlUpdate, (novo_valor, num_estoque))       
        mydb.close()
        
        return True
    except:
        return False

def Delet_Estoque(estoqueID):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()

        num_estoque = estoqueID
        sqlDelete = f"DELETE FROM Estoque WHERE Num_estoque = '{num_estoque}'"
        mycursor.execute(sqlDelete) 
        mydb.close()
        
        return True
    except:
        return False

def Estoque(op):
    if op == 1:
        print("\n--- CADASTRAR ESTOQUE ---")
        atributos = Atributos_Estoque()
        valores = []
        for atributo in atributos:
            valor = input(f"{atributo}: ")
            valores.append(valor)
        Cadastrar_Estoque(tuple(valores))
        print("Estoque cadastrado com sucesso!")
    
    elif op == 2:
        print("\n--- ALTERAR ESTOQUE ---")
        Printar_Estoque()
        posicao = int(input("Escolha o estoque: "))
        Printar_Atributos()
        atributo = int(input("Escolha o atributo: "))
        novo_valor = input("Novo valor: ")
        Update_Estoque(posicao, atributo, novo_valor)
        print("Estoque alterado com sucesso!")
    
    elif op == 3:
        print("\n--- DELETAR ESTOQUE ---")
        Printar_Estoque()
        posicao = int(input("Escolha o estoque: "))
        Delet_Estoque(posicao)
        print("Estoque deletado com sucesso!")
    
    elif op == 4:
        print("\n--- LISTAR ESTOQUES ---")
        Printar_Estoque()