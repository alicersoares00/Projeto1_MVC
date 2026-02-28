import uuid
from datetime import datetime

class Pessoa():
    def __init__(self, cpf, nome, idade, email):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.email = email

class Cliente(Pessoa):
    def __init__(self, cpf, nome, idade, email):
        super().__init__(cpf, nome, idade, email)

class Funcionario(Pessoa):
    def __init__(self, cpf, nome, idade, email):
        super().__init__(cpf, nome, idade, email)

class Categoria():
    def __init__(self, nome, id_categoria):
        self.nome = nome
        self.id_categoria = id_categoria 

class Fornecedor():
    def __init__(self, nome, id_fornecedor, categorias):
        self.nome = nome
        self.id_fornecedor = id_fornecedor
        self.categorias = categorias

class Produto():
    def __init__(self, nome, id_produto, preco, categoria: Categoria, fornecedor: Fornecedor):
        self.nome = nome
        self.id_produto = id_produto
        self.preco = preco
        self.categoria = categoria 
        self.fornecedor = fornecedor 

class Venda:
    def __init__(self, cliente, produtos, total, data=None, id_venda=None):
        self.id_venda = id_venda or str(uuid.uuid4())
        self.cliente = cliente.__dict__   # transforma em dict
        self.produtos = [p.__dict__ for p in produtos]
        self.total = total
        self.data = data or datetime.now()

    



