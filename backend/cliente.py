import conexaoBD

def Listar_Cliente():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Cliente")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

def Printar_Clientes():
    clientes = Listar_Cliente()
    for n in range(len(clientes)):
        print(f"{n+1}- {clientes[n]}")

def Atributos_Cliente():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SHOW COLUMNS FROM Cliente")
    atributos = mycursor.fetchall()
    mydb.close()
    colunas = []
    for n in range(len(atributos)):
        colunas.append(atributos[n][0])
    return colunas

def Printar_Atributos():
    clientes = Atributos_Cliente()
    for n in range(len(clientes)):
        print(f"{n+1}- {clientes[n]}")

def Cadastrar_Cliente(valores): 
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    colunas_lista = Atributos_Cliente()
    colunas_string = ",".join(colunas_lista)
    
    placeholders = ",".join(["%s"] * len(colunas_lista))

    sqlInsert = f"INSERT INTO Cliente ({colunas_string}) VALUES ({placeholders})"

    mycursor.execute(sqlInsert, valores)
    mydb.commit()
    mydb.close()

def Update_Cliente(Cliente_posi, atributo_posi, novo_valor):
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    myresult = Listar_Cliente()
            
    if Cliente_posi > 0 and Cliente_posi <= len(myresult):
        cliente = myresult[Cliente_posi-1]
        cpf = cliente[0]

        atributos = Atributos_Cliente()

        if atributo_posi > 0 and atributo_posi <= len(atributos):
            coluna = atributos[atributo_posi-1]
            sqlUpdate = f"UPDATE Cliente SET {coluna} = %s WHERE CPF = %s"
            mycursor.execute(sqlUpdate, (novo_valor, cpf))
            mydb.commit()
    mydb.close()

def Delet_Cliente(Cliente_posi):
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    myresult = Listar_Cliente()
            
    if Cliente_posi > 0 and Cliente_posi <= len(myresult):
        cliente = myresult[Cliente_posi-1]
        cpf = cliente[0]
        sqlDelete = f"DELET FROM Cliente WHERE CPF = '{cpf}'"
        mycursor.execute(sqlDelete)
        mydb.commit()

        
def Cliente(op):
    if op == 1:
        print("\n--- CADASTRAR CLIENTE ---")
        atributos = Atributos_Cliente()
        valores = []
        for atributo in atributos:
            valor = input(f"{atributo}: ")
            valores.append(valor)
        Cadastrar_Cliente(tuple(valores))
        print("Cliente cadastrado com sucesso!")
    
    elif op == 2:
        print("\n--- ALTERAR CLIENTE ---")
        Printar_Clientes()
        posicao = int(input("Escolha o cliente: "))
        Printar_Atributos()
        atributo = int(input("Escolha o atributo: "))
        novo_valor = input("Novo valor: ")
        Update_Cliente(posicao, atributo, novo_valor)
        print("Cliente alterado com sucesso!")
    
    elif op == 3:
        print("\n--- DELETAR CLIENTE ---")
        Printar_Clientes()
        posicao = int(input("Escolha o cliente: "))
        Delet_Cliente(posicao)
        print("Cliente deletado com sucesso!")
    elif op == 4:
        print("\n--- LISTAR CLIENTES ---")
        Printar_Clientes()
