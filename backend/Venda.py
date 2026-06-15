import conexaoBD

def Listar_Venda():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Venda")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

def Printar_Vendas():
    vendas = Listar_Venda()
    for n in range(len(vendas)):
        print(f"{n+1}- {vendas[n]}")

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

def Printar_Atributos():
    vendas = Atributos_Venda()
    for n in range(len(vendas)):
        print(f"{n+1}- {vendas[n]}")

def Cadastrar_Venda(valores): 
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    colunas_lista = Atributos_Venda()
    colunas_string = ",".join(colunas_lista)
    
    placeholders = ",".join(["%s"] * len(colunas_lista))

    sqlInsert = f"INSERT INTO Venda ({colunas_string}) VALUES ({placeholders})"

    mycursor.execute(sqlInsert, valores)
    mydb.commit()
    mydb.close()

def Update_Venda(Venda_posi, atributo_posi, novo_valor):
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    myresult = Listar_Venda()
            
    if Venda_posi > 0 and Venda_posi <= len(myresult):
        venda = myresult[Venda_posi-1]
        num_venda = venda[0]

        atributos = Atributos_Venda()

        if atributo_posi > 0 and atributo_posi <= len(atributos):
            coluna = atributos[atributo_posi-1]
            sqlUpdate = f"UPDATE Venda SET {coluna} = %s WHERE Num_venda = %s"
            mycursor.execute(sqlUpdate, (novo_valor, num_venda))
            mydb.commit()
    mydb.close()

def Delet_Venda(Venda_posi):
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    myresult = Listar_Venda()
            
    if Venda_posi > 0 and Venda_posi <= len(myresult):
        venda = myresult[Venda_posi-1]
        num_venda = venda[0]
        sqlDelete = f"DELETE FROM Venda WHERE Num_venda = '{num_venda}'"
        mycursor.execute(sqlDelete)
        mydb.commit()
    mydb.close()

def Venda(op):
    if op == 1:
        print("\n--- CADASTRAR VENDA ---")
        atributos = Atributos_Venda()
        valores = []
        for atributo in atributos:
            valor = input(f"{atributo}: ")
            valores.append(valor)
        Cadastrar_Venda(tuple(valores))
        print("Venda cadastrada com sucesso!")
    
    elif op == 2:
        print("\n--- ALTERAR VENDA ---")
        Printar_Vendas()
        posicao = int(input("Escolha a venda: "))
        Printar_Atributos()
        atributo = int(input("Escolha o atributo: "))
        novo_valor = input("Novo valor: ")
        Update_Venda(posicao, atributo, novo_valor)
        print("Venda alterada com sucesso!")
    
    elif op == 3:
        print("\n--- DELETAR VENDA ---")
        Printar_Vendas()
        posicao = int(input("Escolha a venda: "))
        Delet_Venda(posicao)
        print("Venda deletada com sucesso!")
    
    elif op == 4:
        print("\n--- LISTAR VENDAS ---")
        Printar_Vendas()