import conexaoBD

def Modelo(op):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        
        mycursor.execute("""CREATE TABLE IF NOT EXISTS Modelo(
                        idModelo INT NOT NULL PRIMARY KEY,
                        Nome VARCHAR(100) NOT NULL,
                        Ano_Modelo INT NOT NULL,
                        Marca_CNPJ VARCHAR(45) NOT NULL,
                        FOREIGN KEY (Marca_CNPJ) REFERENCES Marca(CNPJ)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
                        ) ENGINE = InnoDB""")
        
        if op == 1:
            print('CADASTRO DE MODELO')
            
            id_modelo = int (input('digite o ID do Modelo: '))
            nome = str (input('digite o nome do modelo:'))
            ano = int (input('digite o Ano do Modelo: '))
            marca_cnpj = str (input('digite o CNPJ da marca: '))

            sqlInsert = 'INSERT INTO Modelo (idModelo, Nome, Ano_Modelo, Marca_CNPJ) VALUES (%s, %s, %s, %s)'
            
            val = (id_modelo, nome, ano, marca_cnpj)
            
            mycursor.execute(sqlInsert, val)
            print(f"\nmodelo '{nome}' cadastrado")
        
        elif op == 2:
            
            print('\nLISTANDO MODELOS:\n')

            mycursor.execute('SELECT * FROM Modelo')
            myresult = mycursor.fetchall()
    
            if len(myresult) == 0:
            
                print('nenhum modelo cadastrado.')
            
            else:
            
                for n in range(len(myresult)):
            
                    print(f"modelo {n+1}: {myresult[n]}")

                n = int(input('escolha o modelo pra alterar: '))
                
                if n > 0 and n <= len(myresult):
                
                    modelo = myresult[n-1]
                    
                    id_modelo = modelo[0]
                    nome = modelo[1]
                    ano = modelo[2]
                    marca_cnpj = modelo[3]
                    
                    print('\nALTERACAO DE MODELO\n')

                    print(f"(1) ID do modelo: {id_modelo}\n(2) nome: {nome}\n(3) ano Modelo: {ano}\n(4) CNPJ da marca: {marca_cnpj}")
                    
                    opcao = int (input('digite a opcao pra alterar: '))
                    
                    escolha = "Nome"
                    if opcao == 1:
                        mudar = int(input('novo ID do Modelo: '))
                        escolha = "idModelo"

                    elif opcao == 2:
                        mudar = str(input('novo Nome: '))
                        escolha = "Nome"

                    elif opcao == 3:
                        mudar = int(input('novo Ano: '))
                        escolha = "Ano_Modelo"
                    else:
                        mudar = str(input('novo CNPJ da Marca: '))
                        escolha = "Marca_CNPJ"

    # aqui faz a
                    if escolha == "idModelo" or escolha == "Ano_Modelo":
                        sqlUpdate = f"UPDATE Modelo SET {escolha} = {mudar} WHERE idModelo = {id_modelo}"
                    else:
                        sqlUpdate = f"UPDATE Modelo SET {escolha} = '{mudar}' WHERE idModelo = {id_modelo}"
                        
                    mycursor.execute(sqlUpdate)
                    print('\nmodelo alterado\n')
                
        elif op == 3:
            
            print('LISTANDO MODELOS')
            
            mycursor.execute("SELECT * FROM Modelo")
            myresult = mycursor.fetchall()
    
            if len(myresult) == 0:
                print('NENHUM MODELO CADASTRADO')
            
            else:
            
                for n in range(len(myresult)):
            
                    print(f"Modelo {n+1}: {myresult[n]}")

                n = int(input('Escolha um modelo para apagar: '))
                
                if n > 0 and n <= len(myresult):
                    modelo = myresult[n-1]

                    id_modelo = modelo[0]
                    nome = modelo[1]
                    ano = modelo[2]
                    marca_cnpj = modelo[3]
                
                    print("DELETANDO MODELO")
            
                    print(f"ID: {id_modelo}\n(1) nome: {nome}\n(2) ano: {ano}\n(3) marca: {marca_cnpj}")
                    
                    confirma = str (input('\napagar modelo (sim/nao): '))

                    if confirma in 'sim':
                        sqlDelete = f"DELETE FROM Modelo WHERE idModelo = {id_modelo}"
                        mycursor.execute(sqlDelete)
                        print('\nModelo removido\n')
                    else:
                        print("processo interrompido")
                        
        mydb.commit()

    except Exception as e:
        print(f"Erro {e}")
