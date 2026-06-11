import conexaoBD
mydb = conexaoBD.conectar()
mycursor = mydb.cursor()

def Listar_Vendedor():
    mycursor.execute("SELECT * FROM Vendedor")
    myresult = mycursor.fetchall()
    
    return myresult

def Printar_Vendedores():
    vendedores = Listar_Vendedor()
    for n in range(len(vendedores)):
        print(f"{n+1}- {vendedores[n]}")

def Atributos_Vendedor():
    mycursor.execute("SHOW COLUMNS FROM Vendedor")
    atributos = mycursor.fetchall()

    colunas = []
    for n in range(len(atributos)):
        colunas.append(atributos[n][0])
    
    return colunas

def Printar_Atributos():
    vendedores = Atributos_Vendedor()
    for n in range(len(vendedores)):
        print(f"{n+1}- {vendedores[n]}")

def Cadastrar_Vendedor(valores): 
    colunas_lista = Atributos_Vendedor()
    colunas_string = ",".join(colunas_lista)
    
    placeholders = ",".join(["%s"] * len(colunas_lista))

    sqlInsert = f"INSERT INTO Vendedor ({colunas_string}) VALUES ({placeholders})"

    mycursor.execute(sqlInsert, valores)

def Update_Vendedor(Vendedor_posi, atributo_posi, novo_valor):
    myresult = Listar_Vendedor()
            
    if Vendedor_posi > 0 and Vendedor_posi <= len(myresult):
        vendedor = myresult[Vendedor_posi-1]
        cpf = vendedor[0]
        atributos = Atributos_Vendedor()

        if atributo_posi > 0 and atributo_posi <= len(atributos):
            coluna = atributos[atributo_posi-1]
            sqlUpdate = f"UPDATE Vendedor SET {coluna} = %s WHERE CPF = %s"
            mycursor.execute(sqlUpdate, (novo_valor, cpf))

def Delet_Vendedor(Vendedor_posi):
    myresult = Listar_Vendedor()
            
    if Vendedor_posi > 0 and Vendedor_posi <= len(myresult):
        vendedor = myresult[Vendedor_posi-1]
        cpf = vendedor[0]
        sqlDelete = f"DELETE FROM Vendedor WHERE CPF = '{cpf}'"
        mycursor.execute(sqlDelete)