import conexaoBD

mydb = conexaoBD.conectar()
mycursor = mydb.cursor()

def Listar_Cliente():
    mycursor.execute("SELECT * FROM Cliente")
    myresult = mycursor.fetchall()
    
    return myresult

def Printar_Clientes():
    clientes = Listar_Cliente()
    for n in range(len(clientes)):
        print(f"{n+1}- {clientes[n]}")

def Atributos_Cliente():
    mycursor.execute("SHOW COLUMNS FROM Cliente")
    atributos = mycursor.fetchall()

    colunas = []
    for n in range(len(atributos)):
        colunas.append(atributos[n][0])
    
    return colunas

def Printar_Atributos():
    clientes = Atributos_Cliente()
    for n in range(len(clientes)):
        print(f"{n+1}- {clientes[n]}")

def Cadastrar_Cliente(valores): 
    colunas_lista = Atributos_Cliente()
    colunas_string = ",".join(colunas_lista)
    
    placeholders = ",".join(["%s"] * len(colunas_lista))

    sqlInsert = f"INSERT INTO Cliente ({colunas_string}) VALUES ({placeholders})"

    mycursor.execute(sqlInsert, valores)

def Update_Cliente(Cliente_posi, atributo_posi, novo_valor):
    myresult = Listar_Cliente()
            
    if Cliente_posi > 0 and Cliente_posi <= len(myresult):
        cliente = myresult[Cliente_posi-1]
        cpf = cliente[0]

        atributos = Atributos_Cliente()

        if atributo_posi > 0 and atributo_posi<=len(atributos):
            coluna = atributos[atributo_posi-1]
            sqlUpdate = f"UPDATE Cliente SET {coluna} = %s WHERE CPF =%s"
            mycursor.execute(sqlUpdate,(novo_valor, cpf))

def Delet_Cliente(Cliente_posi):
    myresult = Listar_Cliente()
            
    if Cliente_posi > 0 and Cliente_posi <= len(myresult):
        cliente = myresult[Cliente_posi-1]
        cpf = cliente[0]
        sqlDelete = f"DELETE FROM Cliente WHERE CPF = '{cpf}'"
        mycursor.execute(sqlDelete)