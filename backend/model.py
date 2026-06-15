import conexaoBD

def Listar_Modelo():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Modelo")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

def Printar_Modelo():
    modelos = Listar_Modelo()
    for n in range(len(modelos)):
        print(f"{n+1}- {modelos[n]}")

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

def Printar_Atributos():
    modelos = Atributos_Modelo()
    for n in range(len(modelos)):
        print(f"{n+1}- {modelos[n]}")

def Cadastrar_Modelo(valores): 
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    colunas_lista = Atributos_Modelo()
    colunas_string = ",".join(colunas_lista)
    
    placeholders = ",".join(["%s"] * len(colunas_lista))

    sqlInsert = f"INSERT INTO Modelo ({colunas_string}) VALUES ({placeholders})"

    mycursor.execute(sqlInsert, valores)
    mydb.commit()
    mydb.close()

def Update_Modelo(Modelo_posi, atributo_posi, novo_valor):
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    myresult = Listar_Modelo()
            
    if Modelo_posi > 0 and Modelo_posi <= len(myresult):
        modelo = myresult[Modelo_posi-1]
        id_modelo = modelo[0]

        atributos = Atributos_Modelo()

        if atributo_posi > 0 and atributo_posi <= len(atributos):
            coluna = atributos[atributo_posi-1]
            sqlUpdate = f"UPDATE Modelo SET {coluna} = %s WHERE idModelo = %s"
            mycursor.execute(sqlUpdate, (novo_valor, id_modelo))
            mydb.commit()
    mydb.close()

def Delet_Modelo(Modelo_posi):
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    myresult = Listar_Modelo()
            
    if Modelo_posi > 0 and Modelo_posi <= len(myresult):
        modelo = myresult[Modelo_posi-1]
        id_modelo = modelo[0]
        sqlDelete = f"DELETE FROM Modelo WHERE idModelo = {id_modelo}"
        mycursor.execute(sqlDelete)
        mydb.commit()
    mydb.close()

def Modelo(op):
    if op == 1:
        print("\n--- CADASTRAR MODELO ---")
        atributos = Atributos_Modelo()
        valores = []
        for atributo in atributos:
            valor = input(f"{atributo}: ")
            valores.append(valor)
        Cadastrar_Modelo(tuple(valores))
        print("Modelo cadastrado com sucesso!")
    
    elif op == 2:
        print("\n--- ALTERAR MODELO ---")
        Printar_Modelo()
        posicao = int(input("Escolha o modelo: "))
        Printar_Atributos()
        atributo = int(input("Escolha o atributo: "))
        novo_valor = input("Novo valor: ")
        Update_Modelo(posicao, atributo, novo_valor)
        print("Modelo alterado com sucesso!")
    
    elif op == 3:
        print("\n--- DELETAR MODELO ---")
        Printar_Modelo()
        posicao = int(input("Escolha o modelo: "))
        Delet_Modelo(posicao)
        print("Modelo deletado com sucesso!")
    
    elif op == 4:
        print("\n--- LISTAR MODELOS ---")
        Printar_Modelo()