import conexaoBD

def Listar_Carros():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Carros")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

def Printar_Carros():
    carros = Listar_Carros()
    for n in range(len(carros)):
        print(f"{n+1}- {carros[n]}")

def Atributos_Carros():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SHOW COLUMNS FROM Carros")
    atributos = mycursor.fetchall()
    mydb.close()
    colunas = []
    for n in range(len(atributos)):
        colunas.append(atributos[n][0])
    return colunas

def Printar_Atributos():
    carros = Atributos_Carros()
    for n in range(len(carros)):
        print(f"{n+1}- {carros[n]}")

def Cadastrar_Carros(valores): 
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        colunas_lista = Atributos_Carros()
        colunas_string = ",".join(colunas_lista)
        
        placeholders = ",".join(["%s"] * len(colunas_lista))

        sqlInsert = f"INSERT INTO Carros ({colunas_string}) VALUES ({placeholders})"

        mycursor.execute(sqlInsert, valores)
        mydb.close()
        return True
    except:
        return False

def Update_Carros(carrosKEy, coluna, novo_valor):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()

        chassi = carrosKEy
        sqlUpdate = f"UPDATE Carros SET {coluna} = %s WHERE Chassi = %s"
        mycursor.execute(sqlUpdate, (novo_valor, chassi))
        mydb.close()
        return True
    except:
        return False

def Delet_Carros(chassi):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
    
        sqlDelete = f"DELETE FROM Carros WHERE Chassi = '{chassi}'"
        mycursor.execute(sqlDelete)
        mydb.close()
        return True
    except:
        return False

def Carros(op):
    if op == 1:
        print("\n--- CADASTRAR CARRO ---")
        atributos = Atributos_Carros()
        valores = []
        for atributo in atributos:
            valor = input(f"{atributo}: ")
            valores.append(valor)
        Cadastrar_Carros(tuple(valores))
        print("Carro cadastrado com sucesso!")
    
    elif op == 2:
        print("\n--- ALTERAR CARRO ---")
        Printar_Carros()
        posicao = int(input("Escolha o carro: "))
        Printar_Atributos()
        atributo = int(input("Escolha o atributo: "))
        novo_valor = input("Novo valor: ")
        Update_Carros(posicao, atributo, novo_valor)
        print("Carro alterado com sucesso!")
    
    elif op == 3:
        print("\n--- DELETAR CARRO ---")
        Printar_Carros()
        posicao = int(input("Escolha o carro: "))
        Delet_Carros(posicao)
        print("Carro deletado com sucesso!")
    
    elif op == 4:
        print("\n--- LISTAR CARROS ---")
        Printar_Carros()