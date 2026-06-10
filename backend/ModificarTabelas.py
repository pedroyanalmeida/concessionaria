from conexaoBD import conectar

mydb = conectar()
mycursor = mydb.cursor()

def Listar_Tabelas():
    mycursor.execute("SHOW TABLES")
    tabelas = mycursor.fetchall()
    return tabelas

def Printar_Tabelas():
    tabelas = Listar_Tabelas()
    print("Tabelas cadastradas: ")
    for n in range(len(tabelas)):
        print(f"{n+1}-"+tabelas[n][0])


def Listar_Atributos(Tabela_Escolhida):
    tabelas = Listar_Tabelas()
    
    if Tabela_Escolhida>0 and Tabela_Escolhida <= len(tabelas):
        tabela = tabelas[Tabela_Escolhida-1][0]

    mycursor.execute(f"SHOW COLUMNS FROM {tabela}")
    atributos = mycursor.fetchall()

    return atributos

def Printar_Atributos(Tabela_Escolhida):
    atributos = Listar_Atributos(Tabela_Escolhida)
    for n in range(len(atributos)):
        print(f"{n+1}-",atributos[n])

def Cadastrar_Atributos(Tabela_Escolhida, atri):
    tabelas = Listar_Tabelas()
    
    if Tabela_Escolhida>0 and Tabela_Escolhida <= len(tabelas):
        tabela = tabelas[Tabela_Escolhida-1][0]
        tipo ="VARCHAR(100)"
                
        sqlAdd = f"ALTER TABLE {tabela} ADD {atri} {tipo}"
        mycursor.execute(sqlAdd)

def Drop_Atributo(tabela_posi, atri):
    tabelas = Listar_Tabelas()
    
    if tabela_posi>0 and tabela_posi <= len(tabelas):
        tabela = tabelas[tabela_posi-1][0]        
        atributos = Listar_Atributos(tabela_posi)

        if atributos[tabela_posi-1][3] != "MUL":
            if atri > 0 and atri < len(atributos):
                coluna = atributos[atri][0]
                sqlDrop = f"ALTER TABLE {tabela} DROP COLUMN IF EXISTS {coluna}"
                mycursor.execute(sqlDrop)
        else:
            print("não pode")

def Rename_Atributo(tabela_posi, atributo_posi, novo_nome):
    tabelas = Listar_Tabelas()
    
    if tabela_posi>0 and tabela_posi <= len(tabelas):
        tabela = tabelas[tabela_posi-1][0]

        atributos = Listar_Atributos(tabela_posi-1)

        if atributo_posi > 0 and atributo_posi <= len(atributos):
            coluna = atributos[atributo_posi][0]
                    
            sqlRename = f"ALTER TABLE {tabela} RENAME COLUMN {coluna} TO {novo_nome}"
            mycursor.execute(sqlRename)

def Drop_Tabela(tabela_posi):
    tabelas = Listar_Tabelas()
    
    if tabela_posi>0 and tabela_posi <= len(tabelas):
        tabela = tabelas[tabela_posi-1][0]
    
        mycursor.execute(f"DROP TABLE IF EXISTS {tabela}")
        print(f"Tabela {tabela} excluída com sucesso!")

Printar_Tabelas()
Drop_Tabela(2)
