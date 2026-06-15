import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import cliente
import carros

entradas_cliente = {}
entradas_carro = {}


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

    confirma = messagebox.askyesno("Confirmar", f"Deseja apagar o cliente de CPF {cpf}?")
    if confirma:
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

    confirma = messagebox.askyesno("Confirmar", f"Deseja apagar o carro de Chassi {chassi}?")
    if confirma:
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


# ===================== POPUP DE EDIÇÃO aqui ele é usado pelas duas telas mas no futuro antes de entregar pro professor alguém poderia dividir pra cada =====================

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


# ===================== JANELA PRINCIPAL =====================

janela = tk.Tk()
janela.title("Agência de Carros")
janela.geometry("950x550")

# --- NAVBAR ---
navbar = tk.Frame(janela, bg="#2c3e50", height=50)
navbar.pack(side=tk.TOP, fill=tk.X)

tk.Button(navbar, text="Cadastrar Cliente", bg="#2c3e50", fg="white", relief=tk.FLAT,
          font=("Arial", 11), padx=15, command=lambda: mostrar_frame(tela_cliente)).pack(side=tk.LEFT)

tk.Button(navbar, text="Carros", bg="#2c3e50", fg="white", relief=tk.FLAT,
          font=("Arial", 11), padx=15, command=lambda: mostrar_frame(tela_carros)).pack(side=tk.LEFT)

tk.Button(navbar, text="Marcas", bg="#2c3e50", fg="white", relief=tk.FLAT,
          font=("Arial", 11), padx=15, command=lambda: mostrar_frame(tela_marcas)).pack(side=tk.LEFT)

tk.Button(navbar, text="Estoque", bg="#2c3e50", fg="white", relief=tk.FLAT,
          font=("Arial", 11), padx=15, command=lambda: mostrar_frame(tela_estoque)).pack(side=tk.LEFT)

# --- CONTAINER ---
container = tk.Frame(janela)
container.pack(fill=tk.BOTH, expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# =====================  TELA CLIENTE =====================

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

# ===================== TELA CARROS =====================

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
