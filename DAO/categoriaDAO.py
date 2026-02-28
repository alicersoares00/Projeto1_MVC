import json
from models import Categoria

class CategoriaDAO:
    def __init__(self, arquivo_json = 'categorias.json'):
        self.arquivo = arquivo_json
    
    def ler(self):
        try:
            with open(self.arquivo, 'r') as arqCat:
                return json.load(arqCat)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def salvar(self, categorias):
        with open(self.arquivo, 'w') as arqCat:
            json.dump(categorias, arqCat, indent=4)
    
    def criar(self, categoria: Categoria):
        categorias = self.ler()
        categorias.append(categoria.__dict__)
        self.salvar(categorias)
    
    def ler_categoria(self, id_categoria):
        categorias = self.ler()
        for c in categorias:
            if c['id_categoria'] == id_categoria:
                return c
        return None
    
    def atualizar(self, categoria: Categoria):
        categorias = self.ler()
        for i, c in enumerate(categorias):
            if c['id_categoria'] == categoria.id_categoria:
                categorias[i] = categoria.__dict__
                self.salvar(categorias)
                return True
        return False
    
    def deletar(self, id_categoria):
        categorias = self.ler()
        categorias_alt = [c for c in categorias if c['id_categoria'] != id_categoria]
        self.salvar(categorias_alt)

