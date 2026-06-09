import conexaoBD

def Estoque(op):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        
        if op == 1: 
            num_estoque = input("Número do estoque: ")
            quantidade = input("Quantidade de carros: ")
            localizacao = input("Localização: ")
            
            sql = "INSERT INTO Estoque (Num_estoque, Quantidade_carros, Localização) VALUES (%s, %s, %s)"
            valores = (num_estoque, quantidade, localizacao)
            mycursor.execute(sql, valores)
            print("Estoque cadastrado com sucesso!")
            
        elif op == 2: 
            print("Listando todos os estoques:")
            
            mycursor.execute("SELECT * FROM Estoque")
            myresult = mycursor.fetchall()
            
            for n in range(len(myresult)):
                print(f"estoque{n+1}: {myresult[n]}")
            
            n = int(input("Escolha um estoque para fazer alteração: "))
            
            if n > 0 and n <= len(myresult):
                estoque = myresult[n-1]
                num_estoque = estoque[0]
                
                print("=" * 40)
                print("      ALTERAÇÃO DE ESTOQUE")
                print("=" * 40)
                
                mycursor.execute(f"SHOW COLUMNS FROM Estoque")
                atributos = mycursor.fetchall()
                
                for n in range(1, len(atributos)):
                    print(f"{n}-" + atributos[n][0])
                
                atri = int(input("Qual atributo deseja alterar: "))
                
                if atri > 0 and atri < len(atributos):
                    coluna = atributos[atri][0]
                    mudar = input(f"{coluna}: ")
                    
                    sqlUpdate = f"UPDATE Estoque SET {coluna} = '{mudar}' WHERE Num_estoque = '{num_estoque}'"
                    mycursor.execute(sqlUpdate)
                    print("Estoque atualizado com sucesso!")
        
        mydb.commit()
        
    except Exception as e:
        print(f"Erro no estoque: {e}")

