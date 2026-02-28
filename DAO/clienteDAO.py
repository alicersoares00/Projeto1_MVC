import json 
from models import Cliente

class ClienteDAO:
    def __init__(self, arquivo_json = 'clientes.json'):
        self.arquivo = arquivo_json
    
    def ler(self):
        try:
            with open(self.arquivo, 'r') as arqC:
                return json.load(arqC)
        except FileNotFoundError:
            return []
    
    def salvar(self, clientes):
        with open(self.arquivo, 'w') as arqC:
            json.dump(clientes, arqC, indent=4)
    
    def criar(self, cliente: Cliente):
        clientes = self.ler()
        clientes.append(cliente.__dict__)
        self.salvar(clientes)
    
    def ler_cliente(self, cpf):
        clientes = self.ler()
        for c in clientes:
            if c['cpf'] == cpf:
                return c
        return None
    
    def atualizar(self, cliente: Cliente):
        clientes = self.ler()
        for i, c in enumerate(clientes):
            if c['cpf'] == cliente.cpf:
                clientes[i] = cliente.__dict__
                self.salvar(clientes)
                return True
        return False
    
    def deletar(self, cpf):
        clientes = self.ler()
        clientes_alt = [c for c in clientes if c['cpf'] != cpf]
        self.salvar(clientes_alt)




        


                    

        
