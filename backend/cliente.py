import conexaoBD

def Cliente(op):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        if op == 1:
            mycursor.execute(f"SHOW COLUMNS FROM Cliente")
            atributos = mycursor.fetchall()

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

            # cpf = str(input("CPF: "))
            # nome = str(input("Nome: "))
            # endereco = str(input("Endereço: "))
            # telefone = str(input("Telefone: "))
            
            # val = (cpf, nome, endereco, telefone)
            mycursor.execute(sqlInsert, val)

        elif op == 2:
            print("Listando todos os cliente:")
            
            mycursor.execute("SELECT * FROM Cliente")
            myresult = mycursor.fetchall()
    
            for n in range(len(myresult)):
                print(f"cliente{n+1}: {myresult[n]}")

            n = int(input("Escolha um cliente para fazer alteração: "))
            
            if n > 0 and n <= len(myresult):
                cliente = myresult[n-1]

                print("=" * 40)
                print("      ALTERAÇÃO DE CLIENTE")
                print("=" * 40)

                for at in cliente:
                    print(at,"\n")

                # print(f"1 - CPF      : {cpf}\n2 - Nome     : {nome}\n3 - Endereço : {endereco}\n4 - Telefone : {telefone}")
                
                # opcao = int(input("Campo para alterar: "))
                
                mycursor.execute(f"SHOW COLUMNS FROM Cliente")
                atributos = mycursor.fetchall()

                for n in range(1,len(atributos)):
                    print(f"{n}-"+atributos[n][0])
                
                atri = int(input("Qual atributo deseja excluir: "))

                if atri > 0 and atri<len(atributos):
                    coluna = atributos[atri][0]

                    mudar = str(input(f"{coluna}: "))
                # escolha = "CPF"
                # if opcao == 1:
                #     mudar = str(input("CPF: "))
                # elif opcao == 2:
                #     mudar = str(input("Nome: "))
                #     escolha = "Nome"
                # elif opcao == 3:
                #     mudar = str(input("Endereco: "))
                #     escolha = "Endereco"
                # else:
                #     mudar = str(input("Telefone: "))
                #     escolha = "Telefone"

                    sqlUpdate = f"UPDATE Cliente SET {coluna} = '{mudar}' WHERE CPF ='{cpf}'"
                    mycursor.execute(sqlUpdate)

        elif op == 3:
            print("Listando todos os cliente:")
            
            mycursor.execute("SELECT * FROM Cliente")
            myresult = mycursor.fetchall()
    
            for n in range(len(myresult)):
                print(f"cliente{n+1}: {myresult[n]}")

            n = int(input("Escolha um cliente para ser apagado no sistema: "))
            
            if n > 0 and n <= len(myresult):
                cliente = myresult[n-1]
                cpf = cliente[0]
                nome = cliente[1]
                endereco = cliente[2]
                telefone = cliente[3]

                print("=" * 40)
                print("      DELETANDO CLIENTE")
                print("=" * 40)

                print(f"1 - CPF      : {cpf}\n2 - Nome     : {nome}\n3 - Endereço : {endereco}\n4 - Telefone : {telefone}")
                
                confirma = str(input("Confirma[S/N]: "))
                if confirma in 'Ss':
                    sqlDelete = f"DELETE FROM Cliente WHERE CPF = '{cpf}'"
                    mycursor.execute(sqlDelete)
        mydb.commit()

    except:
        print("Erro no cliente")


Cliente(2)