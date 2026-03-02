from models import Venda, Cliente, Produto
from DAO.caixaDAO import CaixaDAO
from datetime import datetime

class CaixaController:
    def __init__(self):
        self.dao = CaixaDAO()

    def registrar_venda(self, cliente: Cliente, produtos: list[Produto], pagamento: float = None):
        # calcula o total
        total = sum(float(p.preco) for p in produtos)
        venda = Venda(cliente, produtos, total)
        self.dao.criar(cliente, produtos, total)
        
        troco = None
        if pagamento is not None:
            troco = round(float(pagamento) - total, 2)

        return venda, troco


    def buscar_venda(self, id_venda: str):
        return self.dao.ler_venda(id_venda)

    def listar_vendas(self):
        return self.dao.listar_vendas()

    def remover_venda(self, id_venda: str):
        self.dao.deletar(id_venda)

    # Relatórios
    def total_vendas(self):
        return self.dao.total_vendas()

    def produtos_mais_vendidos(self):
        return self.dao.produtos_mais_vendidos()

    def clientes_que_mais_compram(self):
        return self.dao.clientes_que_mais_compram()