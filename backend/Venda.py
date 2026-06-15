import conexaoBD
from cliente import Printar_Clientes


mydb = conexaoBD.conectar()
mycursor = mydb.cursor()

def Listar_Venda():
    mycursor.execute("SELECT * FROM Venda")
    myresult = mycursor.fetchall()
    
    for n in range(len(myresult)):
        print(f"Venda{n+1}: {myresult[n]}")
    
    return myresult

def Printar_Vendas():
    vendas = Listar_Venda()
    for n in range(len(vendas)):
        print(f"{n+1}- {vendas[n]}")

def Atributos_Venda():
    mycursor.execute("SHOW COLUMNS FROM Venda")
    atributos = mycursor.fetchall()

    colunas = []
    for n in range(len(atributos)):
        colunas.append(atributos[n][0])
    
    return colunas

def Printar_Atributos():
    vendas = Atributos_Venda()
    for n in range(len(vendas)):
        print(f"{n+1}- {vendas[n]}")

def Cadastrar_Venda(valores): 
    colunas_lista = Atributos_Venda()
    colunas_string = ",".join(colunas_lista)
    
    placeholders = ",".join(["%s"] * len(colunas_lista))

    sqlInsert = f"INSERT INTO Venda ({colunas_string}) VALUES ({placeholders})"

    mycursor.execute(sqlInsert, valores)

def Update_Venda(Venda_posi, atributo_posi, novo_valor):
    myresult = Listar_Venda()
            
    if Venda_posi > 0 and Venda_posi <= len(myresult):
        venda = myresult[Venda_posi-1]
        numeVenda = venda[0]

        atributos = Atributos_Venda()

        if atributo_posi > 0 and atributo_posi<=len(atributos):
            coluna = atributos[atributo_posi-1]
            sqlUpdate = f"UPDATE Venda SET {coluna} = %s WHERE NumVenda =%s"
            mycursor.execute(sqlUpdate,(novo_valor, numeVenda))

def Delet_Venda(Venda_posi):
    myresult = Listar_Venda()
               
    if Venda_posi > 0 and Venda_posi <= len(myresult):
        venda = myresult[Venda_posi-1]
        numVenda = venda[0]
        sqlDelete = f"DELETE FROM Venda WHERE NumVenda = '{numVenda}'"
        mycursor.execute(sqlDelete)

Printar_Atributos()
print("===========================")
Cadastrar_Venda(('1','10/06/2026', '5000', '11111', '18%', '1'))