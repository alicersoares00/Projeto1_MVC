from DAO.clienteDAO import ClienteDAO
from models import Cliente
class ClienteController:
    def __init__(self):
        self.dao = ClienteDAO()

    def cadastrar_cliente(self, cpf, nome, idade, email):
        
        if len(nome) > 0 and len(cpf) > 10 and idade > 0:

            cliente = Cliente(cpf, nome, idade, email)
            self.dao.criar(cliente)
            return cliente
        else:
            raise ValueError('Nome, cpf ou idade com valores inválidos!!')
    
    def buscar_cliente(self, cpf):
        return self.dao.ler_cliente(cpf)
    
    def atualizar_cliente(self, cpf, nome, idade, email):
        cliente = Cliente(cpf, nome, idade, email)
        if not self.dao.atualizar(cliente):
            raise ValueError("não encontrado")
        return cliente

    def remover_cliente(self, cpf):
        self.dao.deletar(cpf)
    
    def listar_clientes(self):
        return self.dao.ler()

