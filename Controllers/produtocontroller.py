from DAO.produtoDAO import ProdutoDAO
from models import Produto
class ProdutoController:
    def __init__(self):
        self.dao = ProdutoDAO()

    def cadastrar_produto(self, nome, id_produto, preco, categoria, fornecedor):
        
        if len(nome) > 0:

            produto = Produto(nome, str(id_produto), preco, categoria, fornecedor)
            self.dao.criar(produto)
            return produto
        else:
            raise ValueError('Nome inválido!!')
    
    def buscar_produto(self, id_produto):
        return self.dao.ler_produto(id_produto)
    
    def atualizar_produto(self, nome, id_produto, preco, categoria, fornecedor):
        produto = Produto(nome, str(id_produto), preco, categoria, fornecedor)
        if not self.dao.atualizar(produto):
            raise ValueError("não encontrado")
        return produto

    def remover_produto(self, id_produto):
        self.dao.deletar(id_produto)
    
    def listar_produtos(self):
        return self.dao.ler()

