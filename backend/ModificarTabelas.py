from conexaoBD import conectar

mydb = conectar()
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")
tabelas = mycursor.fetchall()

print("Tabelas cadastradas: ")
for n in range(len(tabelas)):
    print(f"{n+1}-"+tabelas[n][0])

n = int(input("Escolha um Tabela para fazer alteração: "))

if n>0 and n <=len(tabelas):
    tabela = tabelas[n-1][0]
    
    op = int(input("Qal opção você deseja(1-ALTER|2-DROP): "))
    
    if op == 1:
        esc = int(input("Que tipo de alteração(1-ADD|2-DROP|3-RENAME): ").upper())
        if esc == 1:
            atri = str(input("Qual atributo? "))
            tipo = str(input("Qual o tipo? ").upper())
            if tipo == "VARCHAR":
                tam = str(input("Qual tamanho do VARCHAR? "))
                tipo += f"({tam})"
            
            sqlAdd = f"ALTER TABLE {tabela} ADD {atri} {tipo}"
            mycursor.execute(sqlAdd)

        elif esc == 2:
            print("Listando os Atributos: ")

            mycursor.execute(f"SHOW COLUMNS FROM {tabela}")
            atributos = mycursor.fetchall()

            for n in range(1,len(atributos)):
                print(f"{n}-"+atributos[n][0])

            atri = int(input("Qual atributo deseja excluir: "))

            if atri > 0 and atri<len(atributos):
                coluna = atributos[atri][0]
                sqlDrop = f"ALTER TABLE {tabela} DROP COLUMN {coluna}"
                mycursor.execute(sqlDrop)
        else:
            mycursor.execute(f"SHOW COLUMNS FROM {tabela}")
            atributos = mycursor.fetchall()

            for n in range(0,len(atributos)):
                print(f"{n+1}-"+atributos[n][0])
            
            atri = int(input("Qual atributo deseja Renomear: "))

            if atri > 0 and atri <=len(atributos):
                coluna = atributos[atri-1][0]
                
                nome = str(input("Qual outro nome: "))
                
                sqlRename = f"ALTER TABLE {tabela} RENAME COLUMN {coluna} TO {nome}"
                mycursor.execute(sqlRename)
        
    elif op == 2:
        mycursor.execute(f"DROP TABLE {tabela}")
    
    mydb.commit()