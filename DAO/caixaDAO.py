import json
from datetime import datetime
import uuid

class CaixaDAO:
    def __init__(self, arquivo_json="vendas.json"):
        self.arquivo = arquivo_json

    # -------------------------
    # Funções básicas de persistência
    # -------------------------
    def ler(self):
        try:
            with open(self.arquivo, "r") as arq:
                return json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def salvar(self, vendas):
        with open(self.arquivo, "w") as arq:
            json.dump(vendas, arq, indent=4)

    # -------------------------
    # CRUD de vendas
    # -------------------------
    def criar(self, cliente, produtos, total):
        vendas = self.ler()
        venda = {
            "id_venda": str(uuid.uuid4()),   # gera ID único
            "cliente": cliente.__dict__,     # objeto Cliente convertido em dict
            "produtos": [p.__dict__ for p in produtos],  # lista de objetos Produto
            "total": total,
            "data": datetime.now().isoformat()
        }
        vendas.append(venda)
        self.salvar(vendas)
        return venda

    def ler_venda(self, id_venda):
        vendas = self.ler()
        for v in vendas:
            if str(v["id_venda"]) == str(id_venda):
                return v
        return None

    def listar_vendas(self):
        return self.ler()

    def deletar(self, id_venda):
        vendas = self.ler()
        vendas_alt = [v for v in vendas if str(v["id_venda"]) != str(id_venda)]
        self.salvar(vendas_alt)

    # -------------------------
    # Relatórios
    # -------------------------
    def total_vendas(self):
        vendas = self.ler()
        return sum(float(v["total"]) for v in vendas)

    def produtos_mais_vendidos(self):
        vendas = self.ler()
        contagem = {}
        for v in vendas:
            for p in v["produtos"]:
                nome = p["nome"]
                qtd = int(p.get("quantidade", 1))  # assume 1 se não tiver campo quantidade
                contagem[nome] = contagem.get(nome, 0) + qtd
        return sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    def clientes_que_mais_compram(self):
        vendas = self.ler()
        contagem = {}
        for v in vendas:
            cliente = v["cliente"]["nome"]
            total = float(v["total"])
            contagem[cliente] = contagem.get(cliente, 0) + total
        return sorted(contagem.items(), key=lambda x: x[1], reverse=True)