import json
from models import Produto

class ProdutoDAO:
    def __init__(self, arquivo_json = 'produtos.json'):
        self.arquivo = arquivo_json
    
    def ler(self):
        try:
            with open(self.arquivo, 'r') as arqP:
                return json.load(arqP)
        except FileNotFoundError:
            return []
    
    def salvar(self, produtos):
        with open(self.arquivo, 'w') as arqP:
            json.dump(produtos, arqP, indent=4)
    
    def criar(self, produto: Produto):
        produtos = self.ler()
        produtos.append(produto.__dict__)
        self.salvar(produtos)
    
    def ler_produto(self, id_produto):
        produtos = self.ler()
        for p in produtos:
            if str(p['id_produto']) == str(id_produto):
                return p
        return None
    
    def atualizar(self, produto: Produto):
        produtos = self.ler()
        for i, p in enumerate(produtos):
            if str(p['id_produto']) == str(produto.id_produto):
                produtos[i] = produto.__dict__
                self.salvar(produtos)
                return True
        return False
    
    def deletar(self, id_produto):
        produtos = self.ler()
        produtos_alt = [p for p in produtos if p['id_produto'] != id_produto]
        self.salvar(produtos_alt)

