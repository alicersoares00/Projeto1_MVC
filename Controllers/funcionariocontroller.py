from DAO.funcionarioDAO import FuncionarioDAO
from models import Funcionario
class FuncionarioController:
    def __init__(self):
        self.dao = FuncionarioDAO()

    def cadastrar_funcionario(self, cpf, nome, idade, email):
        
        if len(nome) > 0 and len(cpf) > 10 and idade > 0:

            funcionario = Funcionario(cpf, nome, idade, email)
            self.dao.criar(funcionario)
            return funcionario
        else:
            raise ValueError('Nome, cpf ou idade com valores inválidos!!')
    
    def buscar_funcionario(self, cpf):
        return self.dao.ler_funcionario(cpf)
    
    def atualizar_funcionario(self, cpf, nome, idade, email):
        funcionario = Funcionario(cpf, nome, idade, email)
        if not self.dao.atualizar(funcionario):
            raise ValueError("não encontrado")
        return funcionario

    def remover_funcionario(self, cpf):
        self.dao.deletar(cpf)
    
    def listar_funcionarios(self):
        return self.dao.ler()

