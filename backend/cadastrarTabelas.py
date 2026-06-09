import conexaoBD

def cadastrar():
    try:
        mydb = conexaoBD.conectar()
        mycursor = mydb.cursor()
        mycursor.execute("""CREATE TABLE IF NOT EXISTS Cliente(
                        CPF VARCHAR(45) NOT NULL PRIMARY KEY,
                        Nome VARCHAR(100) NOT NULL,
                        Endereco VARCHAR(100) NOT NULL,
                        Telefone VARCHAR(100) NOT NULL 
                        ) ENGINE = InnoDB""")
        
        mycursor.execute("""CREATE TABLE IF NOT EXISTS Vendedor(
                        CPF VARCHAR(45) NOT NULL PRIMARY KEY,
                        Nome VARCHAR(100) NOT NULL,
                        Senha VARCHAR(100) NOT NULL,
                        Login VARCHAR(100) NOT NULL
                        ) ENGINE = InnoDB""")
        
        mycursor.execute("""CREATE TABLE IF NOT EXISTS Venda(
                        NumVenda INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                        DataVenda VARCHAR(45) NOT NULL,
                        Valor VARCHAR(45) NOT NULL,
                        ClienteCPF VARCHAR(45) NOT NULL,
                        NumParcelas VARCHAR(45) NOT NULL,
                        VendedorCPF VARCHAR(45) NOT NULL,

                        INDEX fk_VENDA_Cliente_idx (ClienteCPF ASC),
                        INDEX fk_VENDA_Vendedor1_idx (VendedorCPF ASC),

                        CONSTRAINT fk_VENDA_Cliente
                            FOREIGN KEY (ClienteCPF)
                            REFERENCES Cliente (CPF)
                            ON DELETE NO ACTION
                            ON UPDATE NO ACTION,

                        CONSTRAINT fk_VENDA_Vendedor1
                            FOREIGN KEY (VendedorCPF)
                            REFERENCES Vendedor (CPF)
                            ON DELETE NO ACTION
                            ON UPDATE NO ACTION
                    ) ENGINE=InnoDB
                    """)
        
        mycursor.execute("""CREATE TABLE IF NOT EXISTS Marca(
                        CNPJ VARCHAR(45) NOT NULL PRIMARY KEY,
                        Nome VARCHAR(100) NOT NULL
                        ) ENGINE=InnoDB""")
        
        mycursor.execute("""CREATE TABLE IF NOT EXISTS Estoque(
                        NumEstoque INT NOT NULL PRIMARY KEY,
                        QuantidadeCarros VARCHAR(45) NOT NULL,
                        Localizacao VARCHAR(100) NOT NULL
                        ) ENGINE = InnoDB""")
        
        mycursor.execute("""CREATE TABLE IF NOT EXISTS Modelo(
                        IDModelo INT NOT NULL PRIMARY KEY,
                        Nome VARCHAR(100) NOT NULL,
                        AnoModelo VARCHAR(45) NOT NULL,                        
                        
                        INDEX fk_Modelo_Marca1_idx (CNPJ ASC),
                        
                        CONSTRAINT fk_Modelo_Marca1
                            FOREIGN KEY (CNPJ)
                            REFERENCES Marca (CNPJ)
                            ON DELETE NO ACTION
                            ON UPDATE NO ACTION
                        )ENGINE = InnoDB""")

        mycursor.execute("""CREATE TABLE IF NOT EXISTS Carros(
                        Chassi VARCHAR(45) NOT NULL PRIMARY KEY,
                        Cor VARCHAR(45) NOT NULL,
                        Preco VARCHAR(45) NOT NULL,
                        NumVenda VARCHAR(45) NOT NULL,
                        NumEstoque VARCHAR(45) NOT NULL,
                        IDModelo VARCHAR(45) NOT NULL,
                        
                        INDEX fk_Carros_Venda1_idx (NumVenda ASC),
                        INDEX fk_Carros_Estoque1_idx (NumEstoque ASC),
                        INDEX fk_Carros_Modelo1_idx (IDModelo ASC),
                        
                        CONSTRAINT fk_Carros_Venda1
                            FOREIGN KEY (NumVenda)
                            REFERENCES Venda (NumVenda)
                            ON DELETE NO ACTION
                            ON UPDATE NO ACTION,
                        
                        CONSTRAINT fk_Carros_Estoque1
                            FOREIGN KEY (NumEstoque)
                            REFERENCES Estoque (NumEstoque)
                            ON DELETE NO ACTION
                            ON UPDATE NO ACTION,
                        
                        CONSTRAINT fk_Carros_Modelo1
                            FOREIGN KEY (IDModelo)
                            REFERENCES Modelo (IDModelo)
                            ON DELETE NO ACTION
                            ON UPDATE NO ACTION
                        )ENGINE = InnoDB""")
    except:
        print("Erro ao cadastrar tabelas")
