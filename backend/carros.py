import conexaoBD

def Carros(op):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        
        if op == 1:
            mycursor.execute(f"SHOW COLUMNS FROM Carros")
            atributos = mycursor.fetchall()

            colunas = ""
            for n in range(len(atributos)):
                colunas += atributos[n][0]
                if n < len(atributos)-1:
                    colunas += ", "

            placeholders = ", ".join(["%s"] * len(atributos))

            sqlInsert = f"INSERT INTO Carros ({colunas}) VALUES ({placeholders})" 

            colunas = colunas.split(",")

            val = tuple()
            for n in range(len(colunas)):
                value = str(input(f"{colunas[n]}: "))
                val += (value,)

            mycursor.execute(sqlInsert, val)
            print("Carro cadastrado com sucesso!")

        elif op == 2:
            print("Listando todos os carros:")
            
            mycursor.execute("SELECT * FROM Carros")
            myresult = mycursor.fetchall()
    
            for n in range(len(myresult)):
                print(f"carro{n+1}: {myresult[n]}")

            n = int(input("Escolha um carro para fazer alteração: "))
            
            if n > 0 and n <= len(myresult):
                carro = myresult[n-1]
                chassi = carro[0]

                print("=" * 40)
                print("      ALTERAÇÃO DE CARRO")
                print("=" * 40)

                for at in carro:
                    print(at,"\n")
                
                mycursor.execute(f"SHOW COLUMNS FROM Carros")
                atributos = mycursor.fetchall()

                for n in range(1, len(atributos)):
                    print(f"{n}-"+atributos[n][0])
                
                atri = int(input("Qual atributo deseja alterar: "))

                if atri > 0 and atri < len(atributos):
                    coluna = atributos[atri][0]

                    mudar = str(input(f"{coluna}: "))

                    sqlUpdate = f"UPDATE Carros SET {coluna} = '{mudar}' WHERE Chassi = '{chassi}'"
                    mycursor.execute(sqlUpdate)
                    print("Carro atualizado com sucesso!")

        elif op == 3:
            print("Listando todos os carros:")
            
            mycursor.execute("SELECT * FROM Carros")
            myresult = mycursor.fetchall()
    
            for n in range(len(myresult)):
                print(f"carro{n+1}: {myresult[n]}")

            n = int(input("Escolha um carro para ser apagado no sistema: "))
            
            if n > 0 and n <= len(myresult):
                carro = myresult[n-1]
                chassi = carro[0]
                cor = carro[1]
                preco = carro[2]
                venda_num = carro[3]
                estoque_num = carro[4]
                modelo_id = carro[5]

                print("=" * 40)
                print("      DELETANDO CARRO")
                print("=" * 40)

                print(f"1 - Chassi: {chassi}\n2 - Cor: {cor}\n3 - Preço: {preco}\n4 - N° Venda: {venda_num}\n5 - N° Estoque: {estoque_num}\n6 - ID Modelo: {modelo_id}")
                
                confirma = str(input("Confirma[S/N]: "))
                if confirma in 'Ss':
                    sqlDelete = f"DELETE FROM Carros WHERE Chassi = '{chassi}'"
                    mycursor.execute(sqlDelete)
                    print("Carro deletado com sucesso!")
        
        mydb.commit()
        
    except Exception as e:
        print(f"Erro no carro: {e}")