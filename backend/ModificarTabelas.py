import conexaoBD

def Listar_Tabelas():
    mydb = conexaoBD.conectar()
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    tabelas = mycursor.fetchall()
    mydb.close()
    return tabelas

def Printar_Tabelas():
    tabelas = Listar_Tabelas()
    print("Tabelas cadastradas: ")
    for n in range(len(tabelas)):
        print(f"{n+1}-"+tabelas[n][0])


def Listar_Atributos(Tabela_Escolhida):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        mycursor.execute(f"SHOW COLUMNS FROM {Tabela_Escolhida}")
        atributos = mycursor.fetchall()
        mydb.close()

        return atributos
    except:
        return False

def Printar_Atributos(Tabela_Escolhida):
    atributos = Listar_Atributos(Tabela_Escolhida)
    for n in range(len(atributos)):
        print(f"{n+1}-",atributos[n])

def Cadastrar_Atributos(Tabela_Escolhida, atributo):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        
        tipo ="VARCHAR(100)"        
        sqlAdd = f"ALTER TABLE {Tabela_Escolhida} ADD {atributo} {tipo}"
        mycursor.execute(sqlAdd)
        mydb.close()
        
        return True
    except:
        return False

def Drop_Atributo(Tabela_Escolhida, atributo):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        atri = Listar_Atributos(Tabela_Escolhida)
        escAtributo = None

        for at in atri:
            if at[0] == atributo:
                escAtributo = atri
                break
        if escAtributo[3] not in ("MUL","PRI"):
            sqlDrop = f"ALTER TABLE {Tabela_Escolhida} DROP COLUMN IF EXISTS {atributo}"
            mycursor.execute(sqlDrop)

        mydb.close()
            
        return True
    except:
        return False
       

def Rename_Atributo(Tabela_Escolhida, atributo, novo_nome):
    try:   
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        atri = Listar_Atributos(Tabela_Escolhida)
        escAtributo = None

        for at in atri:
            if at[0] == atributo:
                escAtributo = atri
                break
        if escAtributo[3] not in ("MUL","PRI"):             
            sqlRename = f"ALTER TABLE {Tabela_Escolhida} RENAME COLUMN {atributo} TO {novo_nome}"
            mycursor.execute(sqlRename)
        mydb.close()

        return True
    except:
        return False

def Drop_Tabela(Tabela_Escolhida):
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        mycursor.execute(f"DROP TABLE IF EXISTS {Tabela_Escolhida}")
        print(f"Tabela {Tabela_Escolhida} excluída com sucesso!")
        mydb.close()

        return True
    except:
        return False