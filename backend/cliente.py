import conexaoBD
mydb = conexaoBD.conectar()
global mycursor = mydb.cursor()
mycursor.autoComi

def Listar_Cliente():
    mycursor.execute(f"SHOW COLUMNS FROM Cliente")
    atributos = mycursor.fetchall()
    for n in range(len(myresult)):
        print(f"cliente{n+1}: {myresult[n]}")
    
    return atributos

def Cadastrar_Cliente():
        mycursor.execute(f"SHOW COLUMNS FROM Cliente")
        atributos = mycursor.fetchall()

        atributos = Listar_Cliente()
        colunas = ""
        for n in range(len(atributos)):
            colunas += atributos[n][0]
            if n < len(atributos)-1:
                colunas += ", "

        placeholders = ", ".join(["%s"] * len(atributos))

        sqlInsert = f"INSERT INTO Cliente ({colunas}) VALUES ({placeholders})" 

        colunas = colunas.split(",")

        val = tuple()
        for n in range(len(colunas)):
            value = str(input(f"{colunas[n]}: "))
            val += (value,)

        mycursor.execute(sqlInsert, val)

def Update_Cliente():
    Listar_Cliente()
    n = int(input("Escolha um cliente para fazer alteração: "))
            
    if n > 0 and n <= len(myresult):
        cliente = myresult[n-1]
        cpf = cliente[0]

        print("=" * 40)
        print("      ALTERAÇÃO DE CLIENTE")
        print("=" * 40)

        for at in cliente:
            print(at)
                
        print("=" * 40)
                
        mycursor.execute(f"SHOW COLUMNS FROM Cliente")
        atributos = mycursor.fetchall()

        for n in range(len(atributos)):
            print(f"{n+1}-"+atributos[n][0])
                
        atri = int(input("Qual atributo deseja excluir: "))

        if atri > 0 and atri<=len(atributos):
            coluna = atributos[atri-1][0]

            mudar = str(input(f"{coluna}: "))

            sqlUpdate = f"UPDATE Cliente SET {coluna} = '{mudar}' WHERE CPF ='{cpf}'"
            mycursor.execute(sqlUpdate)

def Delet_Cliente():
    n = int(input("Escolha um cliente para ser apagado no sistema: "))
            
    if n > 0 and n <= len(myresult):
        cliente = myresult[n-1]
        cpf = cliente[0]

        print("=" * 40)
        print("      DELETANDO CLIENTE")
        print("=" * 40)

        print(f"1 - CPF      : {cpf}\n2 - Nome     : {nome}\n3 - Endereço : {endereco}\n4 - Telefone : {telefone}")
                
        confirma = str(input("Confirma[S/N]: "))
        if confirma in 'Ss':
            sqlDelete = f"DELETE FROM Cliente WHERE CPF = '{cpf}'"
            mycursor.execute(sqlDelete)

def Cliente(op):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        if op == 1:
            
            # colunas = ""
            # for n in range(len(atributos)):
            #     colunas += atributos[n][0]
            #     if n < len(atributos)-1:
            #         colunas += ", "

            # placeholders = ", ".join(["%s"] * len(atributos))

            # sqlInsert = f"INSERT INTO Cliente ({colunas}) VALUES ({placeholders})" 

            # colunas = colunas.split(",")

            # val = tuple()
            # for n in range(len(colunas)):
            #     value = str(input(f"{colunas[n]}: "))
            #     val += (value,)

            # mycursor.execute(sqlInsert, val)

        elif op == 2:
            print("Listando todos os cliente:")
            
            mycursor.execute("SELECT * FROM Cliente")
            myresult = mycursor.fetchall()
    
            # for n in range(len(myresult)):
            #     print(f"cliente{n+1}: {myresult[n]}")

            # n = int(input("Escolha um cliente para fazer alteração: "))
            
            # if n > 0 and n <= len(myresult):
            #     cliente = myresult[n-1]
            #     cpf = cliente[0]

            #     print("=" * 40)
            #     print("      ALTERAÇÃO DE CLIENTE")
            #     print("=" * 40)

            #     for at in cliente:
            #         print(at)
                
            #     print("=" * 40)
                
            #     mycursor.execute(f"SHOW COLUMNS FROM Cliente")
            #     atributos = mycursor.fetchall()

            #     for n in range(len(atributos)):
            #         print(f"{n+1}-"+atributos[n][0])
                
            #     atri = int(input("Qual atributo deseja excluir: "))

            #     if atri > 0 and atri<=len(atributos):
            #         coluna = atributos[atri-1][0]

            #         mudar = str(input(f"{coluna}: "))

            #         sqlUpdate = f"UPDATE Cliente SET {coluna} = '{mudar}' WHERE CPF ='{cpf}'"
            #         mycursor.execute(sqlUpdate)

        elif op == 3:
            print("Listando todos os cliente:")
            
            mycursor.execute("SELECT * FROM Cliente")
            myresult = mycursor.fetchall()
    
            for n in range(len(myresult)):
                print(f"cliente{n+1}: {myresult[n]}")

        #     n = int(input("Escolha um cliente para ser apagado no sistema: "))
            
        #     if n > 0 and n <= len(myresult):
        #         cliente = myresult[n-1]
        #         cpf = cliente[0]
        #         nome = cliente[1]
        #         endereco = cliente[2]
        #         telefone = cliente[3]

        #         print("=" * 40)
        #         print("      DELETANDO CLIENTE")
        #         print("=" * 40)

        #         print(f"1 - CPF      : {cpf}\n2 - Nome     : {nome}\n3 - Endereço : {endereco}\n4 - Telefone : {telefone}")
                
        #         confirma = str(input("Confirma[S/N]: "))
        #         if confirma in 'Ss':
        #             sqlDelete = f"DELETE FROM Cliente WHERE CPF = '{cpf}'"
        #             mycursor.execute(sqlDelete)
        # mydb.commit()

    except:
        print("Erro no cliente")


Cliente(2)