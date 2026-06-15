import conexaoBD

def Listar_Marca():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Marca")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

def Printar_Marca():
    marcas = Listar_Marca()
    for n in range(len(marcas)):
        print(f"{n+1}- {marcas[n]}")

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

def Printar_Atributos():
    marcas = Atributos_Marca()
    for n in range(len(marcas)):
        print(f"{n+1}- {marcas[n]}")

def Cadastrar_Marca(valores): 
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    colunas_lista = Atributos_Marca()
    colunas_string = ",".join(colunas_lista)
    
    placeholders = ",".join(["%s"] * len(colunas_lista))

    sqlInsert = f"INSERT INTO Marca ({colunas_string}) VALUES ({placeholders})"

    mycursor.execute(sqlInsert, valores)
    mydb.commit()
    mydb.close()

def Update_Marca(Marca_posi, atributo_posi, novo_valor):
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    myresult = Listar_Marca()
            
    if Marca_posi > 0 and Marca_posi <= len(myresult):
        marca = myresult[Marca_posi-1]
        cnpj = marca[0]

        atributos = Atributos_Marca()

        if atributo_posi > 0 and atributo_posi <= len(atributos):
            coluna = atributos[atributo_posi-1]
            sqlUpdate = f"UPDATE Marca SET {coluna} = %s WHERE CNPJ = %s"
            mycursor.execute(sqlUpdate, (novo_valor, cnpj))
            mydb.commit()
    mydb.close()

def Delet_Marca(Marca_posi):
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    myresult = Listar_Marca()
            
    if Marca_posi > 0 and Marca_posi <= len(myresult):
        marca = myresult[Marca_posi-1]
        cnpj = marca[0]
        sqlDelete = f"DELETE FROM Marca WHERE CNPJ = '{cnpj}'"
        mycursor.execute(sqlDelete)
        mydb.commit()
    mydb.close()

def Marca(op):
    if op == 1:
        print("\n--- CADASTRAR MARCA ---")
        atributos = Atributos_Marca()
        valores = []
        for atributo in atributos:
            valor = input(f"{atributo}: ")
            valores.append(valor)
        Cadastrar_Marca(tuple(valores))
        print("Marca cadastrada com sucesso!")
    
    elif op == 2:
        print("\n--- ALTERAR MARCA ---")
        Printar_Marca()
        posicao = int(input("Escolha a marca: "))
        Printar_Atributos()
        atributo = int(input("Escolha o atributo: "))
        novo_valor = input("Novo valor: ")
        Update_Marca(posicao, atributo, novo_valor)
        print("Marca alterada com sucesso!")
    
    elif op == 3:
        print("\n--- DELETAR MARCA ---")
        Printar_Marca()
        posicao = int(input("Escolha a marca: "))
        Delet_Marca(posicao)
        print("Marca deletada com sucesso!")
    
    elif op == 4:
        print("\n--- LISTAR MARCAS ---")
        Printar_Marca()