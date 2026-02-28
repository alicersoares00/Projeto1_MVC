from DAO.categoriaDAO import CategoriaDAO
from models import Categoria
class CategoriaController:
    def __init__(self):
        self.dao = CategoriaDAO()

    def cadastrar_categoria(self, nome, id_categoria):
        
        if len(nome) > 0:
            categoria = Categoria(nome, str(id_categoria))
            self.dao.criar(categoria)
            return categoria
        else:
            raise ValueError('Nome inválido!!')
    
    def buscar_categoria(self, id_categoria):
        return self.dao.ler_categoria(id_categoria)
    
    def atualizar_categoria(self, nome, id_categoria):
        categoria = Categoria(nome, id_categoria)
        if not self.dao.atualizar(categoria):
            raise ValueError("não encontrado")
        return categoria

    def remover_categoria(self, id_categoria):
        self.dao.deletar(id_categoria)
    
    def listar_categorias(self):
        return self.dao.ler()

