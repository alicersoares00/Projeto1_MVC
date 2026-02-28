from DAO.fornecedorDAO import FornecedorDAO
from models import Fornecedor, Categoria

class FornecedorController:
    def __init__(self):
        self.dao = FornecedorDAO()

    def cadastrar_fornecedor(self, nome, id_fornecedor, categorias):
        
        if len(nome) > 0:

            fornecedor = Fornecedor(nome, id_fornecedor, categorias)
            self.dao.criar(fornecedor)
            return fornecedor
        else:
            raise ValueError('Nome inválido!!')
    
    def buscar_fornecedor(self, id_fornecedor):
        return self.dao.ler_fornecedor(id_fornecedor)
    
    def atualizar_fornecedor(self, nome, id_fornecedor, categorias):
        fornecedor = Fornecedor(nome, id_fornecedor, categorias)
        if not self.dao.atualizar(fornecedor):
            raise ValueError("não encontrado")
        return fornecedor

    def remover_fornecedor(self, id_fornecedor):
        self.dao.deletar(id_fornecedor)
    
    def listar_fornecedores(self):
        return self.dao.ler()

