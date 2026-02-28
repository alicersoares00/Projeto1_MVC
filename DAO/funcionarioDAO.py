import json
from models import Funcionario

class FuncionarioDAO:
    def __init__(self, arquivo_json = 'funcionarios.json'):
        self.arquivo = arquivo_json
    
    def ler(self):
        try:
            with open(self.arquivo, 'r') as arqF:
                return json.load(arqF)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def criar(self, funcionario: Funcionario):
        funcionarios = self.ler()
        funcionarios.append(funcionario.__dict__)
        self.salvar(funcionarios)
    
    def salvar(self, funcionarios: list):
        with open(self.arquivo, 'w') as arqF:
            json.dump(funcionarios, arqF, indent=4)
    
    def ler_funcionario(self, cpf):
        funcionarios = self.ler()
        for f in funcionarios:
            if f['cpf'] == cpf:
                return f
        return None
    
    def atualizar(self, funcionario: Funcionario):
        funcionarios = self.ler()
        for i, f in enumerate(funcionarios):
            if f['cpf'] == funcionario.cpf:
                funcionarios[i] = funcionario.__dict__
                self.salvar(funcionarios)
                return True
        return False
    
    def deletar(self, cpf):
        funcionarios = self.ler()
        funcionarios_alt = [f for f in funcionarios if f['cpf'] != cpf]
        self.salvar(funcionarios_alt)

