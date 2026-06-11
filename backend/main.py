import conexaoBD
import cliente
import Vendedor
import Venda
import estoque
import carros
import marca
import model

def limpar_tela():
    print("\n" * 50)

def menu_principal():
    while True:
        print("=" * 50)
        print("        AGÊNCIA DE CARROS - SISTEMA")
        print("=" * 50)
        print("1 - Clientes")
        print("2 - Vendedores")
        print("3 - Vendas")
        print("4 - Estoque")
        print("5 - Carros")
        print("6 - Marcas")
        print("7 - Modelos")
        print("0 - Sair")
        print("=" * 50)
        
        try:
            op = int(input("Escolha uma opção: "))
            
            if op == 0:
                print("Saindo do sistema...")
                break
            elif op == 1:
                menu_cliente()
            elif op == 2:
                menu_vendedor()
            elif op == 3:
                menu_venda()
            elif op == 4:
                menu_estoque()
            elif op == 5:
                menu_carro()
            elif op == 6:
                menu_marca()
            elif op == 7:
                menu_modelo()
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um número válido!")

def menu_cliente():
    while True:
        print("\n" + "=" * 40)
        print("        CLIENTES")
        print("=" * 40)
        print("1 - Cadastrar cliente")
        print("2 - Alterar cliente")
        print("3 - Deletar cliente")
        print("4 - Listar clientes")
        print("0 - Voltar")
        print("=" * 40)
        
        try:
            op = int(input("Escolha: "))
            if op == 0:
                break
            elif op == 1:
                cliente.Cliente(1)
            elif op == 2:
                cliente.Cliente(2)
            elif op == 3:
                cliente.Cliente(3)
            elif op == 4:
                cliente.Cliente(4)
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um número válido!")
            
def menu_vendedor():
    while True:
        print("\n" + "=" * 40)
        print("        VENDEDORES")
        print("=" * 40)
        print("1 - Cadastrar vendedor")
        print("2 - Alterar vendedor")
        print("3 - Deletar vendedor")
        print("0 - Voltar")
        print("=" * 40)
        
        try:
            op = int(input("Escolha: "))
            if op == 0:
                break
            elif op == 1:
                vendedor.Vendedor(1)
            elif op == 2:
                vendedor.Vendedor(2)
            elif op == 3:
                vendedor.Vendedor(3)
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um número válido!")

def menu_venda():
    while True:
        print("\n" + "=" * 40)
        print("        VENDAS")
        print("=" * 40)
        print("1 - Cadastrar venda")
        print("2 - Alterar venda")
        print("3 - Deletar venda")
        print("0 - Voltar")
        print("=" * 40)
        
        try:
            op = int(input("Escolha: "))
            if op == 0:
                break
            elif op == 1:
                venda.Venda(1)
            elif op == 2:
                venda.Venda(2)
            elif op == 3:
                venda.Venda(3)
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um número válido!")

def menu_estoque():
    while True:
        print("\n" + "=" * 40)
        print("        ESTOQUE")
        print("=" * 40)
        print("1 - Cadastrar estoque")
        print("2 - Alterar estoque")
        print("3 - Deletar estoque")
        print("0 - Voltar")
        print("=" * 40)
        
        try:
            op = int(input("Escolha: "))
            if op == 0:
                break
            elif op == 1:
                estoque.Estoque(1)
            elif op == 2:
                estoque.Estoque(2)
            elif op == 3:
                estoque.Estoque(3)
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um número válido!")

def menu_carro():
    while True:
        print("\n" + "=" * 40)
        print("        CARROS")
        print("=" * 40)
        print("1 - Cadastrar carro")
        print("2 - Alterar carro")
        print("3 - Deletar carro")
        print("0 - Voltar")
        print("=" * 40)
        
        try:
            op = int(input("Escolha: "))
            if op == 0:
                break
            elif op == 1:
                carros.Carros(1)
            elif op == 2:
                carros.Carros(2)
            elif op == 3:
                carros.Carros(3)
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um número válido!")

def menu_marca():
    while True:
        print("\n" + "=" * 40)
        print("        MARCAS")
        print("=" * 40)
        print("1 - Cadastrar marca")
        print("2 - Alterar marca")
        print("3 - Deletar marca")
        print("0 - Voltar")
        print("=" * 40)
        
        try:
            op = int(input("Escolha: "))
            if op == 0:
                break
            elif op == 1:
                marca.Marca(1)
            elif op == 2:
                marca.Marca(2)
            elif op == 3:
                marca.Marca(3)
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um número válido!")

def menu_modelo():
    while True:
        print("\n" + "=" * 40)
        print("        MODELOS")
        print("=" * 40)
        print("1 - Cadastrar modelo")
        print("2 - Alterar modelo")
        print("3 - Deletar modelo")
        print("0 - Voltar")
        print("=" * 40)
        
        try:
            op = int(input("Escolha: "))
            if op == 0:
                break
            elif op == 1:
                modelo.Modelo(1)
            elif op == 2:
                modelo.Modelo(2)
            elif op == 3:
                modelo.Modelo(3)
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um número válido!")

if __name__ == "__main__":
    menu_principal()