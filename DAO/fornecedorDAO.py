import json
from models import Fornecedor

class FornecedorDAO:
    def __init__(self, arquivo_json = 'fornecedores.json'):
        self.arquivo = arquivo_json
    
    def ler(self):
        try:
            with open(self.arquivo, 'r') as arqFor:
                return json.load(arqFor)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def salvar(self, fornecedores):
        with open(self.arquivo, 'w') as arqFor:
            json.dump(fornecedores, arqFor, indent=4)
    
    def criar(self, fornecedor: Fornecedor):
        fornecedores = self.ler()
        fornecedores.append(fornecedor.__dict__)
        self.salvar(fornecedores)
    
    def ler_fornecedor(self, id_fornecedor):
        fornecedores = self.ler()
        for f in fornecedores:
            if f['id_fornecedor'] == id_fornecedor:
                return f
        return None
    
    def atualizar(self, fornecedor: Fornecedor):
        fornecedores = self.ler()
        for i, f in enumerate(fornecedores):
            if f['id_fornecedor'] == fornecedor.id_fornecedor:
                fornecedores[i] = fornecedor.__dict__
                self.salvar(fornecedores)
                return True
        return False
    
    def deletar(self, id_fornecedor):
        fornecedores = self.ler()
        fornecedores_alt = [f for f in fornecedores if f['id_fornecedor'] != id_fornecedor]
        self.salvar(fornecedores_alt)

