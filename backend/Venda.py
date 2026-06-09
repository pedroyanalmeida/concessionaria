import conexaoBD
mydb = conexaoBD.conectar()
mycursor = mydb.cursor()

def Listar_Venda():
    mycursor.execute("SELECT * FROM Venda")
    myresult = mycursor.fetchall()
    
    for n in range(len(myresult)):
        print(f"Venda{n+1}: {myresult[n]}")
    
    return myresult

def Cadastrar_Venda():
        mycursor.execute(f"SHOW COLUMNS FROM Venda")
        atributos = mycursor.fetchall()

        colunas = ""
        for n in range(len(atributos)):
            colunas += atributos[n][0]
            if n < len(atributos)-1:
                colunas += ","

        placeholders = ",".join(["%s"] * len(atributos))

        sqlInsert = f"INSERT INTO Venda ({colunas}) VALUES ({placeholders})" 

        colunas = colunas.split(",")

        val = tuple()
        for n in range(len(colunas)):
            value = str(input(f"{colunas[n]}: "))
            val += (value,)

        mycursor.execute(sqlInsert, val)

def Update_Venda():
    myresult = Listar_Venda()
    n = int(input("Escolha um Venda para fazer alteração: "))
            
    if n > 0 and n <= len(myresult):
        venda = myresult[n-1]
        cpf = Venda[0]

        print("=" * 40)
        print("      ALTERAÇÃO DE Venda")
        print("=" * 40)

        for at in venda:
            print(at)
                
        print("=" * 40)
                
        mycursor.execute(f"SHOW COLUMNS FROM Venda")
        atributos = mycursor.fetchall()

        for n in range(len(atributos)):
            print(f"{n+1}-"+atributos[n][0])
                
        atri = int(input("Qual atributo deseja excluir: "))

        if atri > 0 and atri<=len(atributos):
            coluna = atributos[atri-1][0]

            mudar = str(input(f"{coluna}: "))

            sqlUpdate = f"UPDATE Venda SET {coluna} = '{mudar}' WHERE CPF ='{cpf}'"
            mycursor.execute(sqlUpdate)

def Delet_Venda():
    myresult = Listar_Venda()
    n = int(input("Escolha um Venda para ser apagado no sistema: "))
            
    if n > 0 and n <= len(myresult):
        venda = myresult[n-1]
        cpf = venda[0]

        print("=" * 40)
        print("      DELETANDO Venda")
        print("=" * 40)
                
        confirma = str(input("Confirma[S/N]: "))
        if confirma in 'Ss':
            sqlDelete = f"DELETE FROM Venda WHERE CPF = '{cpf}'"
            mycursor.execute(sqlDelete)

Cadastrar_Venda()