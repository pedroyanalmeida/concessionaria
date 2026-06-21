import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

import cliente
import carros
import modelo
import relatorio

entradas_cliente = {}
entradas_carro = {}
entradas_modelo = {}


def mostrar_frame(frame):
    frame.tkraise()


# ===================== TELA CLIENTE =====================

def acao_cadastrar_cliente():
    valores = []
    for atributo, caixa in entradas_cliente.items():
        texto = caixa.get()
        if not texto:
            messagebox.showwarning("Aviso", f"O campo {atributo} não pode ficar vazio!")
            return
        valores.append(texto)

    sucesso = cliente.Cadastrar_Cliente(valores)
    if sucesso:
        messagebox.showinfo("Sucesso", "Cliente salvo com sucesso!")
        for caixa in entradas_cliente.values():
            caixa.delete(0, tk.END)
        atualizar_tabela_cliente()
    else:
        messagebox.showerror("Erro", "Não foi possível cadastrar.")


def atualizar_tabela_cliente():
    for linha in tabela_cliente.get_children():
        tabela_cliente.delete(linha)
    dados = cliente.Listar_Cliente()
    if dados:
        for linha_banco in dados:
            tabela_cliente.insert("", tk.END, values=linha_banco)


def apagar_cliente():
    selecionado = tabela_cliente.focus()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um cliente na tabela!")
        return
    valores = tabela_cliente.item(selecionado)["values"]
    cpf = valores[0]
    if messagebox.askyesno("Confirmar", f"Deseja apagar o cliente de CPF {cpf}?"):
        cliente.Delet_Cliente(cpf)
        atualizar_tabela_cliente()


def editar_cliente():
    selecionado = tabela_cliente.focus()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um cliente na tabela!")
        return
    valores = tabela_cliente.item(selecionado)["values"]
    abrir_popup_edicao(colunas_cliente, valores, cliente.Update_Cliente,
                       valores[0], atualizar_tabela_cliente)


# ===================== TELA CARRO =====================

def acao_cadastrar_carro():
    valores = []
    for atributo, caixa in entradas_carro.items():
        texto = caixa.get()
        if not texto:
            messagebox.showwarning("Aviso", f"O campo {atributo} não pode ficar vazio!")
            return
        valores.append(texto)

    sucesso = carros.Cadastrar_Carro(valores)
    if sucesso:
        messagebox.showinfo("Sucesso", "Carro salvo com sucesso!")
        for caixa in entradas_carro.values():
            caixa.delete(0, tk.END)
        atualizar_tabela_carro()
    else:
        messagebox.showerror("Erro", "Não foi possível cadastrar.")


def atualizar_tabela_carro():
    for linha in tabela_carro.get_children():
        tabela_carro.delete(linha)
    dados = carros.Listar_Carro()
    if dados:
        for linha_banco in dados:
            tabela_carro.insert("", tk.END, values=linha_banco)


def apagar_carro():
    selecionado = tabela_carro.focus()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um carro na tabela!")
        return
    valores = tabela_carro.item(selecionado)["values"]
    chassi = valores[0]
    if messagebox.askyesno("Confirmar", f"Deseja apagar o carro de Chassi {chassi}?"):
        carros.Delet_Carro(chassi)
        atualizar_tabela_carro()


def editar_carro():
    selecionado = tabela_carro.focus()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um carro na tabela!")
        return
    valores = tabela_carro.item(selecionado)["values"]
    abrir_popup_edicao(colunas_carro, valores, carros.Update_Carro,
                       valores[0], atualizar_tabela_carro)


# ===================== TELA MODELO =====================

def acao_cadastrar_modelo():
    valores = []
    for atributo, caixa in entradas_modelo.items():
        texto = caixa.get()
        if not texto:
            messagebox.showwarning("Aviso", f"O campo {atributo} não pode ficar vazio!")
            return
        valores.append(texto)

    sucesso = modelo.Cadastrar_Modelo(valores)
    if sucesso:
        messagebox.showinfo("Sucesso", "Modelo salvo com sucesso!")
        for caixa in entradas_modelo.values():
            caixa.delete(0, tk.END)
        atualizar_tabela_modelo()
    else:
        messagebox.showerror("Erro", "Não foi possível cadastrar. Verifique se a Marca (CNPJ) existe.")


def atualizar_tabela_modelo():
    for linha in tabela_modelo.get_children():
        tabela_modelo.delete(linha)
    dados = modelo.Listar_Modelo()
    if dados:
        for linha_banco in dados:
            tabela_modelo.insert("", tk.END, values=linha_banco)


def apagar_modelo():
    selecionado = tabela_modelo.focus()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um modelo na tabela!")
        return
    valores = tabela_modelo.item(selecionado)["values"]
    id_mod = valores[0]
    if messagebox.askyesno("Confirmar", f"Deseja apagar o modelo de ID {id_mod}?"):
        modelo.Delet_Modelo(id_mod)
        atualizar_tabela_modelo()


def editar_modelo():
    selecionado = tabela_modelo.focus()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um modelo na tabela!")
        return
    valores = tabela_modelo.item(selecionado)["values"]
    abrir_popup_edicao(colunas_modelo, valores, modelo.Update_Modelo,
                       valores[0], atualizar_tabela_modelo)


# ===================== POPUP DE EDIÇÃO (usado por todas as telas) =====================

def abrir_popup_edicao(colunas, valores, funcao_update, id_registro, funcao_atualizar):
    popup = tk.Toplevel()
    popup.title("Editar")
    popup.geometry("300x400")

    caixas = {}
    for i in range(len(colunas)):
        tk.Label(popup, text=f"{colunas[i]}:").pack(anchor=tk.W, padx=15)
        caixa = tk.Entry(popup, width=30)
        caixa.insert(0, valores[i])
        caixa.pack(pady=3, padx=15)
        caixas[colunas[i]] = caixa

    def salvar():
        for i in range(1, len(colunas)):
            coluna = colunas[i]
            novo_valor = caixas[coluna].get()
            funcao_update(id_registro, coluna, novo_valor)
        messagebox.showinfo("Sucesso", "Dados atualizados!")
        popup.destroy()
        funcao_atualizar()

    tk.Button(popup, text="Salvar", bg="green", fg="white",
              command=salvar, width=15).pack(pady=20)


# ===================== TELA RELATÓRIOS =====================

def mostrar_relatorio(colunas, dados):
    tabela_rel.delete(*tabela_rel.get_children())
    tabela_rel["columns"] = colunas
    for coluna in colunas:
        tabela_rel.heading(coluna, text=coluna)
        tabela_rel.column(coluna, width=140)
    for linha in dados:
        tabela_rel.insert("", tk.END, values=linha)


def rel_top3_vendedores():
    mostrar_relatorio(["Vendedor", "Total de vendas"], relatorio.top3_vendedores())


def rel_top3_modelos():
    mostrar_relatorio(["Modelo", "Marca", "Total vendidos"], relatorio.top3_modelos())


def rel_carros_por_preco():
    mostrar_relatorio(["Preço", "Modelo", "Marca", "Cor", "Ano"], relatorio.carros_por_preco())


def rel_total_carros():
    mostrar_relatorio(["Total de carros"], relatorio.total_carros())


def rel_mais_caro():
    mostrar_relatorio(["Preço mais caro"], relatorio.carro_mais_caro())


def rel_mais_barato():
    mostrar_relatorio(["Preço mais barato"], relatorio.carro_mais_barato())


def rel_vendas_por_cliente():
    mostrar_relatorio(["Cliente", "Total de compras"], relatorio.vendas_por_cliente())


def rel_marca_mais_modelos():
    mostrar_relatorio(["Marca", "Qtd de modelos"], relatorio.marca_com_mais_modelos())


def rel_buscar_cliente():
    nome = simpledialog.askstring("Buscar", "Digite parte do nome do cliente:")
    if nome:
        mostrar_relatorio(["CPF", "Nome", "Endereço", "Telefone"],
                          relatorio.buscar_cliente_por_nome(nome))


def rel_carros_por_cor():
    cor = simpledialog.askstring("Buscar", "Digite a cor:")
    if cor:
        mostrar_relatorio(["Chassi", "Cor", "Preço"], relatorio.carros_por_cor(cor))


def rel_carros_acima_preco():
    valor = simpledialog.askstring("Buscar", "Mostrar carros acima de qual preço?")
    if valor:
        mostrar_relatorio(["Chassi", "Cor", "Preço"], relatorio.carros_acima_preco(valor))


# ===================== JANELA PRINCIPAL =====================

janela = tk.Tk()
janela.title("Agência de Carros")
janela.geometry("980x600")

navbar = tk.Frame(janela, bg="#2c3e50", height=50)
navbar.pack(side=tk.TOP, fill=tk.X)

tk.Button(navbar, text="Cadastrar Cliente", bg="#2c3e50", fg="white", relief=tk.FLAT,
          font=("Arial", 11), padx=15, command=lambda: mostrar_frame(tela_cliente)).pack(side=tk.LEFT)

tk.Button(navbar, text="Carros", bg="#2c3e50", fg="white", relief=tk.FLAT,
          font=("Arial", 11), padx=15, command=lambda: mostrar_frame(tela_carros)).pack(side=tk.LEFT)

tk.Button(navbar, text="Modelos", bg="#2c3e50", fg="white", relief=tk.FLAT,
          font=("Arial", 11), padx=15, command=lambda: mostrar_frame(tela_modelos)).pack(side=tk.LEFT)

tk.Button(navbar, text="Marcas", bg="#2c3e50", fg="white", relief=tk.FLAT,
          font=("Arial", 11), padx=15, command=lambda: mostrar_frame(tela_marcas)).pack(side=tk.LEFT)

tk.Button(navbar, text="Estoque", bg="#2c3e50", fg="white", relief=tk.FLAT,
          font=("Arial", 11), padx=15, command=lambda: mostrar_frame(tela_estoque)).pack(side=tk.LEFT)

tk.Button(navbar, text="Relatórios", bg="#2c3e50", fg="white", relief=tk.FLAT,
          font=("Arial", 11), padx=15, command=lambda: mostrar_frame(tela_relatorios)).pack(side=tk.LEFT)

container = tk.Frame(janela)
container.pack(fill=tk.BOTH, expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# ===================== MONTAGEM TELA CLIENTE =====================

tela_cliente = tk.Frame(container)
tela_cliente.grid(row=0, column=0, sticky="nsew")

frame_esq_cli = tk.Frame(tela_cliente, padx=15, pady=15)
frame_esq_cli.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(frame_esq_cli, text="NOVO CLIENTE", font=("Arial", 12, "bold")).pack(pady=10)

colunas_cliente = cliente.Atributos_Cliente()
for coluna in colunas_cliente:
    tk.Label(frame_esq_cli, text=f"{coluna}:").pack(anchor=tk.W)
    nova_caixa = tk.Entry(frame_esq_cli, width=30)
    nova_caixa.pack(pady=2)
    entradas_cliente[coluna] = nova_caixa

tk.Button(frame_esq_cli, text="Cadastrar", bg="green", fg="white",
          command=acao_cadastrar_cliente, width=15).pack(pady=20)

frame_dir_cli = tk.Frame(tela_cliente, padx=15, pady=15)
frame_dir_cli.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Label(frame_dir_cli, text="CLIENTES CADASTRADOS", font=("Arial", 12, "bold")).pack(pady=10)

tabela_cliente = ttk.Treeview(frame_dir_cli, columns=colunas_cliente, show="headings")
for coluna in colunas_cliente:
    tabela_cliente.heading(coluna, text=coluna)
    tabela_cliente.column(coluna, width=120)
tabela_cliente.pack(fill=tk.BOTH, expand=True)

botoes_cli = tk.Frame(frame_dir_cli)
botoes_cli.pack(pady=10)
tk.Button(botoes_cli, text="Editar", bg="#2980b9", fg="white",
          command=editar_cliente, width=12).pack(side=tk.LEFT, padx=5)
tk.Button(botoes_cli, text="Apagar", bg="#c0392b", fg="white",
          command=apagar_cliente, width=12).pack(side=tk.LEFT, padx=5)

atualizar_tabela_cliente()

# ===================== MONTAGEM TELA CARROS =====================

tela_carros = tk.Frame(container)
tela_carros.grid(row=0, column=0, sticky="nsew")

frame_esq_car = tk.Frame(tela_carros, padx=15, pady=15)
frame_esq_car.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(frame_esq_car, text="NOVO CARRO", font=("Arial", 12, "bold")).pack(pady=10)

colunas_carro = carros.Atributos_Carro()
for coluna in colunas_carro:
    tk.Label(frame_esq_car, text=f"{coluna}:").pack(anchor=tk.W)
    nova_caixa = tk.Entry(frame_esq_car, width=30)
    nova_caixa.pack(pady=2)
    entradas_carro[coluna] = nova_caixa

tk.Button(frame_esq_car, text="Cadastrar", bg="green", fg="white",
          command=acao_cadastrar_carro, width=15).pack(pady=20)

frame_dir_car = tk.Frame(tela_carros, padx=15, pady=15)
frame_dir_car.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Label(frame_dir_car, text="CARROS CADASTRADOS", font=("Arial", 12, "bold")).pack(pady=10)

tabela_carro = ttk.Treeview(frame_dir_car, columns=colunas_carro, show="headings")
for coluna in colunas_carro:
    tabela_carro.heading(coluna, text=coluna)
    tabela_carro.column(coluna, width=100)
tabela_carro.pack(fill=tk.BOTH, expand=True)

botoes_car = tk.Frame(frame_dir_car)
botoes_car.pack(pady=10)
tk.Button(botoes_car, text="Editar", bg="#2980b9", fg="white",
          command=editar_carro, width=12).pack(side=tk.LEFT, padx=5)
tk.Button(botoes_car, text="Apagar", bg="#c0392b", fg="white",
          command=apagar_carro, width=12).pack(side=tk.LEFT, padx=5)

atualizar_tabela_carro()

# ===================== MONTAGEM TELA MODELOS =====================

tela_modelos = tk.Frame(container)
tela_modelos.grid(row=0, column=0, sticky="nsew")

frame_esq_mod = tk.Frame(tela_modelos, padx=15, pady=15)
frame_esq_mod.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(frame_esq_mod, text="NOVO MODELO", font=("Arial", 12, "bold")).pack(pady=10)

colunas_modelo = modelo.Atributos_Modelo()
for coluna in colunas_modelo:
    tk.Label(frame_esq_mod, text=f"{coluna}:").pack(anchor=tk.W)
    nova_caixa = tk.Entry(frame_esq_mod, width=30)
    nova_caixa.pack(pady=2)
    entradas_modelo[coluna] = nova_caixa

tk.Button(frame_esq_mod, text="Cadastrar", bg="green", fg="white",
          command=acao_cadastrar_modelo, width=15).pack(pady=20)

frame_dir_mod = tk.Frame(tela_modelos, padx=15, pady=15)
frame_dir_mod.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Label(frame_dir_mod, text="MODELOS CADASTRADOS", font=("Arial", 12, "bold")).pack(pady=10)

tabela_modelo = ttk.Treeview(frame_dir_mod, columns=colunas_modelo, show="headings")
for coluna in colunas_modelo:
    tabela_modelo.heading(coluna, text=coluna)
    tabela_modelo.column(coluna, width=100)
tabela_modelo.pack(fill=tk.BOTH, expand=True)

botoes_mod = tk.Frame(frame_dir_mod)
botoes_mod.pack(pady=10)
tk.Button(botoes_mod, text="Editar", bg="#2980b9", fg="white",
          command=editar_modelo, width=12).pack(side=tk.LEFT, padx=5)
tk.Button(botoes_mod, text="Apagar", bg="#c0392b", fg="white",
          command=apagar_modelo, width=12).pack(side=tk.LEFT, padx=5)

atualizar_tabela_modelo()

# ===================== MONTAGEM TELA RELATÓRIOS =====================

tela_relatorios = tk.Frame(container)
tela_relatorios.grid(row=0, column=0, sticky="nsew")

frame_rel = tk.Frame(tela_relatorios, padx=15, pady=15)
frame_rel.pack(fill=tk.BOTH, expand=True)

tk.Label(frame_rel, text="RELATÓRIOS", font=("Arial", 12, "bold")).pack(pady=10)

frame_botoes_rel = tk.Frame(frame_rel)
frame_botoes_rel.pack(fill=tk.X, pady=5)

lista_botoes_rel = [
    ("Top 3 vendedores", rel_top3_vendedores),
    ("Top 3 modelos", rel_top3_modelos),
    ("Carros por preço", rel_carros_por_preco),
    ("Total de carros", rel_total_carros),
    ("Mais caro", rel_mais_caro),
    ("Mais barato", rel_mais_barato),
    ("Vendas por cliente", rel_vendas_por_cliente),
    ("Marca com + modelos", rel_marca_mais_modelos),
    ("Buscar cliente", rel_buscar_cliente),
    ("Carros por cor", rel_carros_por_cor),
    ("Carros acima de preço", rel_carros_acima_preco),
]

for texto, funcao in lista_botoes_rel:
    tk.Button(frame_botoes_rel, text=texto, command=funcao,
              bg="#2980b9", fg="white", width=18).pack(side=tk.LEFT, padx=3, pady=3)

tabela_rel = ttk.Treeview(frame_rel, show="headings")
tabela_rel.pack(fill=tk.BOTH, expand=True, pady=10)

# ===================== TELA MARCAS =====================

tela_marcas = tk.Frame(container)
tela_marcas.grid(row=0, column=0, sticky="nsew")
tk.Label(tela_marcas, text="TELA DE MARCAS", font=("Arial", 14, "bold")).pack(pady=20)

# ===================== TELA ESTOQUE =====================

tela_estoque = tk.Frame(container)
tela_estoque.grid(row=0, column=0, sticky="nsew")
tk.Label(tela_estoque, text="TELA DE ESTOQUE", font=("Arial", 14, "bold")).pack(pady=20)

mostrar_frame(tela_cliente)

janela.mainloop()
