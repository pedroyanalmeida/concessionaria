import conexaoBD

def Listar_Vendedor():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Vendedor")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

def Printar_Vendedores():
    vendedores = Listar_Vendedor()
    for n in range(len(vendedores)):
        print(f"{n+1}- {vendedores[n]}")

def Atributos_Vendedor():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SHOW COLUMNS FROM Vendedor")
    atributos = mycursor.fetchall()
    mydb.close()

    colunas = []
    for n in range(len(atributos)):
        colunas.append(atributos[n][0])
    
    return colunas

def Printar_Atributos():
    vendedores = Atributos_Vendedor()
    for n in range(len(vendedores)):
        print(f"{n+1}- {vendedores[n]}")

def Cadastrar_Vendedor(valores):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        colunas_lista = Atributos_Vendedor()
        colunas_string = ",".join(colunas_lista)
        
        placeholders = ",".join(["%s"] * len(colunas_lista))

        sqlInsert = f"INSERT INTO Vendedor ({colunas_string}) VALUES ({placeholders})"

        mycursor.execute(sqlInsert, valores)
        mydb.close()
        
        return True
    except:
        return False

def Update_Vendedor(vendedorCPF, coluna, novo_valor):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        cpf = vendedorCPF
        sqlUpdate = f"UPDATE Vendedor SET {coluna} = %s WHERE CPF = %s"
        mycursor.execute(sqlUpdate, (novo_valor, cpf))
        mydb.close()

        return True
    except:
        return False

def Delet_Vendedor(vendedorCPF):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        cpf = vendedorCPF
        sqlDelete = f"DELETE FROM Vendedor WHERE CPF = '{cpf}'"
        mycursor.execute(sqlDelete)
        mydb.close()
        return True
    except:
        return False
    
def Vendedor(op):
    if op == 1:
        print("\n--- CADASTRAR VENDEDOR ---")
        atributos = Atributos_Vendedor()
        valores = []
        for atributo in atributos:
            valor = input(f"{atributo}: ")
            valores.append(valor)
        Cadastrar_Vendedor(tuple(valores))
        print("Vendedor cadastrado com sucesso!")
    
    elif op == 2:
        print("\n--- ALTERAR VENDEDOR ---")
        Printar_Vendedores()
        posicao = int(input("Escolha o vendedor: "))
        Printar_Atributos()
        atributo = int(input("Escolha o atributo: "))
        novo_valor = input("Novo valor: ")
        Update_Vendedor(posicao, atributo, novo_valor)
        print("Vendedor alterado com sucesso!")
    
    elif op == 3:
        print("\n--- DELETAR VENDEDOR ---")
        Printar_Vendedores()
        posicao = int(input("Escolha o vendedor: "))
        Delet_Vendedor(posicao)
        print("Vendedor deletado com sucesso!")
    elif op == 4:
        print("\n--- LISTAR VENDEDORES ---")
        Printar_Vendedores()