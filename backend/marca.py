import conexaoBD

def Marca(op):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        
        mycursor.execute("""CREATE TABLE IF NOT EXISTS Marca(
                        CNPJ VARCHAR(45) NOT NULL PRIMARY KEY,
                        Nome VARCHAR(100) NOT NULL,
                        Pais_origem VARCHAR(45) NOT NULL
                        ) ENGINE = InnoDB""")
        
        if op == 1:

            print('CADASTRO DE MARCA')
            
            cnpj = str(input('Digite o CNPJ da Marca: '))
            nome = str(input('Digite o Nome da Marca (Ex: Fiat, Toyota): '))
            pais = str(input('Digite o País de Origem da Marca: '))

            sqlInsert = 'INSERT INTO Marca (CNPJ, Nome, Pais_origem) VALUES (%s, %s, %s)'
            val = (cnpj, nome, pais)
            
            mycursor.execute(sqlInsert, val)
            print(f"\nmarca '{nome}' cadastrada")
        
        elif op == 2:
        
            print('\nLISTANDO MARCAS:\n')
            mycursor.execute('SELECT * FROM Marca')
            myresult = mycursor.fetchall()
    
            if len(myresult) == 0:
                
                print('nenhuma marca cadastrada.')
            
            else:

                for n in range(len(myresult)):
                    print(f"marca {n+1}: {myresult[n]}")

                n = int (input('Escolha a marca para alterar: '))
                if n > 0 and n <= len(myresult):
                    marca = myresult[n-1]

                    cnpj = marca[0]
                    nome = marca[1]
                    pais = marca[2]
                    
                    print('\nALTERACAO DE MARCA\n')
                    print(f"(1) CNPJ: {cnpj}\n(2) Nome: {nome}\n(3) pais de Origem: {pais}")
                    
                    opcao = int (input('digite a opcao que deseja alterar: '))
                    
                    escolha = "Nome"
                    if opcao == 1:

                        mudar = str(input('novo CNPJ da Marca: '))
                        escolha = "CNPJ"
                        
                    elif opcao == 2:

                        mudar = str(input('novo Nome: '))
                        escolha = "Nome"
                    
                    else:
                        mudar = str(input('novo Pais de Origem: '))
                        escolha = "Pais_origem"

                    sqlUpdate = f"UPDATE Marca SET {escolha} = '{mudar}' WHERE CNPJ = '{cnpj}'"
                        
                    mycursor.execute(sqlUpdate)
                    print('\nmarca alterada com sucesso!\n')
        
        elif op == 3:
            print('LISTANDO MARCAS')
        
            mycursor.execute("SELECT * FROM Marca")
            myresult = mycursor.fetchall()
    
            if len(myresult) == 0:
                print('NENHUMA MARCA CADASTRADA')
        
            else:
        
                for n in range(len(myresult)):
        
                    print(f"marca {n+1}: {myresult[n]}")

                n = int(input('escolha uma marca pra apagar: '))
                
                if n > 0 and n <= len(myresult):
                    marca = myresult[n-1]
                    
                    cnpj = marca[0]
                    nome = marca[1]
                    pais = marca[2]
                
                    print("DELETANDO MARCA")
                    print(f"CNPJ: {cnpj}\nNome: {nome}\nPaís: {pais}")
                    
                    confirma = str(input('\napagar modelo (sim/nao): '))
                    
                    if confirma in 'sim':
                    
                        sqlDelete = f"DELETE FROM Marca WHERE CNPJ = '{cnpj}'"
                        mycursor.execute(sqlDelete)
                        print('\nmarca removida\n')
                    
                    else:
                    
                        print("o processo foi interrompido")
                        
        
        mydb.commit()

    except Exception as e:
        print(f"erro {e}")
