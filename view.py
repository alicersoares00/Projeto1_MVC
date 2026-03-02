from Controllers.clientecontroller import ClienteController
from Controllers.funcionariocontroller import FuncionarioController
from Controllers.categoriacontroller import CategoriaController
from Controllers.fornecedorcontroller import FornecedorController
from Controllers.produtocontroller import ProdutoController
from Controllers.caixacontroller import CaixaController
from models import Cliente, Produto
from DAO.clienteDAO import ClienteDAO
from DAO.produtoDAO import ProdutoDAO

def menu_cliente():
    controller = ClienteController()

    while True:
        print("\n--- MENU CLIENTE ---")
        print("1. Cadastrar cliente")
        print("2. Buscar cliente")
        print("3. Atualizar cliente")
        print("4. Remover cliente")
        print("5. Listar todos")
        print("6. Sair")
        print("7. Voltar pro menu geral")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            cpf = input("CPF: ")
            email = input("Email: ")
            try:
                cliente = controller.cadastrar_cliente(cpf, nome, idade, email)
                print("Cliente cadastrado:", cliente.__dict__)
            except ValueError as e:
                print("Erro:", e)

        elif opcao == "2":
            cpf = input("CPF: ")
            cliente = controller.buscar_cliente(cpf)
            print("Resultado:", cliente if cliente else "Não encontrado")

        elif opcao == "3":
            cpf = input("CPF: ")
            nome = input("Novo nome: ")
            idade = int(input("Nova idade: "))
            email = input("Novo email: ")
            try:
                cliente = controller.atualizar_cliente(cpf, nome, idade, email)
                print("Cliente atualizado:", cliente.__dict__)
            except ValueError as e:
                print("Erro:", e)

        elif opcao == "4":
            cpf = input("CPF: ")
            controller.remover_cliente(cpf)
            print("Cliente removido")
        
        elif opcao == '5':
            print('CLIENTES:')
            for cliente in controller.listar_clientes():
                print(cliente)

        elif opcao == "6":
            break

        elif opcao == "7":
            return menu_geral()

def menu_funcionario():
    controller = FuncionarioController()

    while True:
        print("\n--- MENU FUNCIONÁRIO ---")
        print("1. Cadastrar funcionário")
        print("2. Buscar funcionário")
        print("3. Atualizar funcionário")
        print("4. Remover funcionário")
        print("5. Listar todos")
        print("6. Sair")
        print("7. Voltar pro menu geral")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            cpf = input("CPF: ")
            email = input("Email: ")
            try:
                funcionario = controller.cadastrar_funcionario(cpf, nome, idade, email)
                print("Funcionário cadastrado:", funcionario.__dict__)
            except ValueError as e:
                print("Erro:", e)

        elif opcao == "2":
            cpf = input("CPF: ")
            funcionario = controller.buscar_funcionario(cpf)
            print("Resultado:", funcionario if funcionario else "Não encontrado")

        elif opcao == "3":
            cpf = input("CPF: ")
            nome = input("Novo nome: ")
            idade = int(input("Nova idade: "))
            email = input("Novo email: ")
            try:
                funcionario = controller.atualizar_funcionario(cpf, nome, idade, email)
                print("Funcionario atualizado:", funcionario.__dict__)
            except ValueError as e:
                print("Erro:", e)

        elif opcao == "4":
            cpf = input("CPF: ")
            controller.remover_funcionario(cpf)
            print("Funcionario removido")
        
        elif opcao == '5':
            print('FUNCIONÁRIOS:')
            for funcionario in controller.listar_funcionarios():
                print(funcionario)

        elif opcao == "6":
            break

        elif opcao == "7":
            return menu_geral()

def menu_categorias():
    controller = CategoriaController()

    while True:
        print("\n--- MENU CATEGORIA ---")
        print("1. Cadastrar categoria")
        print("2. Buscar categoria")
        print("3. Atualizar categoria")
        print("4. Remover categoria")
        print("5. Listar categorias")
        print("6. Sair")
        print("7. Voltar pro menu geral")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            id_categoria = int(input('ID da categoria: '))
            try:
                categoria = controller.cadastrar_categoria(nome, id_categoria)
                print("Categoria cadastrada:", categoria.__dict__)
            except ValueError as e:
                print("Erro:", e)

        elif opcao == "2":
            id_categoria = input("id_categoria: ")
            categoria = controller.buscar_categoria(id_categoria)
            print("Resultado:", categoria if categoria else "Não encontrado")

        elif opcao == "3":
            id_categoria = input("ID da categoria: ")
            nome = input("Novo nome: ")
            
            try:
                categoria = controller.atualizar_categoria(nome, id_categoria)
                print("Categoria atualizada:", categoria.__dict__)
            except ValueError as e:
                print("Erro:", e)

        elif opcao == "4":
            id_categoria = input("ID da categoria: ")
            controller.remover_categoria(id_categoria)
            print("Categoria removida")
        
        elif opcao == '5':
            print('CATEGORIAS:')
            for categoria in controller.listar_categorias():
                print(categoria)

        elif opcao == "6":
            break

        elif opcao == "7":
            return menu_geral()

def menu_fornecedores():
    controller = FornecedorController()

    while True:
        print("\n--- MENU FORNECEDOR ---")
        print("1. Cadastrar fornecedor")
        print("2. Buscar fornecedor")
        print("3. Atualizar fornecedor")
        print("4. Remover fornecedor")
        print("5. Listar todos")
        print("6. Sair")
        print("7. Voltar pro menu geral")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            id_fornecedor = input("ID do fornecedor: ")
            categorias = input("Categorias fornecidas: "). split(',')
            categorias = [c.strip() for c in categorias]
            try:
                fornecedor = controller.cadastrar_fornecedor(nome, id_fornecedor, categorias)
                print("Fornecedor cadastrado:", fornecedor.__dict__)
            except ValueError as e:
                print("Erro:", e)

        elif opcao == "2":
            id_fornecedor = input("ID do fornecedor: ")
            fornecedor = controller.buscar_fornecedor(id_fornecedor)
            print("Resultado:", fornecedor if fornecedor else "Não encontrado")

        elif opcao == "3":
            id_fornecedor = input("ID do fornecedor: ")
            nome = input("Novo nome: ")
            categorias = input("Nova categoria: ")
            try:
                fornecedor = controller.atualizar_fornecedor(nome, id_fornecedor, categorias)
                print("Fornecedor atualizado:", fornecedor.__dict__)
            except ValueError as e:
                print("Erro:", e)

        elif opcao == "4":
            id_fornecedor = input("ID do fornecedor: ")
            controller.remover_fornecedor(id_fornecedor)
            print("Fornecedor removido")
        
        elif opcao == '5':
            print('FORNECEDORES:')
            for fornecedor in controller.listar_fornecedores():
                print(fornecedor)

        elif opcao == "6":
            break

        elif opcao == "7":
            return menu_geral()
        
def menu_produtos():
    controller = ProdutoController()

    while True:
        print("\n--- MENU PRODUTOS ---")
        print("1. Cadastrar produto")
        print("2. Buscar produto")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Listar todos")
        print("6. Sair")
        print("7. Voltar pro menu geral")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")    #preco, categoria: Categoria, fornecedor: Fornecedor
            id_produto = int(input("ID do produto: "))
            preco = input("Preço: ")
            categoria = input("Categoria: ")
            fornecedor = input('Fornecedor: ')
            try:
                produto = controller.cadastrar_produto(nome, id_produto, preco, categoria, fornecedor)
                print("Produto cadastrado:", produto.__dict__)
            except ValueError as e:
                print("Erro:", e)

        elif opcao == "2":
            id_produto = input("ID do produto: ")
            produto = controller.buscar_produto(id_produto)
            print("Resultado:", produto if produto else "Não encontrado")

        elif opcao == "3":
            id_produto = input("ID do produto: ")
            nome = input("Novo nome: ")
            preco = int(input("Novo preco: "))
            categoria = input("Nova categoria: ")
            fornecedor = input("Novo fornecedor: ")
            try:
                produto = controller.atualizar_produto(nome, id_produto, preco, categoria, fornecedor)
                print("Produto atualizado:", produto.__dict__)
            except ValueError as e:
                print("Erro:", e)

        elif opcao == "4": 
            id_produto = input("ID do produto: ")
            controller.remover_produto(id_produto)
            print("Produto removido")
        
        elif opcao == '5':
            print('PRODUTOS:')
            for produto in controller.listar_produtos():
                print(produto)

        elif opcao == "6":
            break

        elif opcao == "7":
            return menu_geral()

def menu_caixa():
    controller = CaixaController()
    dao_cliente = ClienteDAO()
    dao_produto = ProdutoDAO()

    while True:
        print("\n--- MENU CAIXA ---")
        print("1. Registrar venda")
        print("2. Buscar venda")
        print("3. Listar vendas")
        print("4. Remover venda")
        print("5. Relatório total de vendas")
        print("6. Produtos mais vendidos")
        print("7. Clientes que mais compram")
        print("8. Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            # Buscar cliente pelo CPF
            cpf_cliente = input("CPF do cliente: ")
            cliente_dict = dao_cliente.ler_cliente(cpf_cliente)
            if not cliente_dict:
                print("Cliente não encontrado!")
                continue
            cliente = Cliente(**cliente_dict)

            # Buscar produtos pelo ID
            produtos = []
            while True:
                id_prod = input("ID do produto (ou ENTER para terminar): ")
                if id_prod == "":
                    break
                produto_dict = dao_produto.ler_produto(id_prod)
                if not produto_dict:
                    print("Produto não encontrado!")
                    continue
                produtos.append(Produto(**produto_dict))

            # Registrar venda
            pagamento = input("Valor pago em dinheiro (ou ENTER se não for dinheiro): ")
            if pagamento.strip() == "":
                venda, troco = controller.registrar_venda(cliente, produtos)
            else:
                venda, troco = controller.registrar_venda(cliente, produtos, float(pagamento))

            print("\n--- RESUMO DA VENDA ---")
            print(f"Cliente: {venda.cliente['nome']}")
            print("Produtos:")
            for p in venda.produtos:
                print(f" - {p['nome']} | R$ {p['preco']}")
            print(f"TOTAL: R$ {venda.total:.2f}")
            if troco is not None:
                print(f"Pagamento: R$ {pagamento}")
                print(f"Troco: R$ {troco:.2f}")

        elif opcao == "2":
            id_venda = input("ID da venda: ")
            venda = controller.buscar_venda(id_venda)
            print("Resultado:", venda if venda else "Não encontrado")

        elif opcao == "3":
            vendas = controller.listar_vendas()
            for v in vendas:
                print(f"Cliente: {v['cliente']['nome']}")
                print("Produtos:")
                for p in v['produtos']:
                    print(f" - {p['nome']} | R$ {p['preco']}")
                print(f"TOTAL: R$ {v['total']:.2f}")
                print("-" * 30)

        elif opcao == "4":
            id_venda = input("ID da venda: ")
            controller.remover_venda(id_venda)
            print("Venda removida.")

        elif opcao == "5":
            print("Total de vendas:", controller.total_vendas())

        elif opcao == "6":
            print("Produtos mais vendidos:", controller.produtos_mais_vendidos())

        elif opcao == "7":
            print("Clientes que mais compram:", controller.clientes_que_mais_compram())

        elif opcao == "8":
            break


def menu_geral():
    print('######## SISTEMA DE GERENCIAMENTO ########')
    setor = int(input('Escolha o setor:\n1.CLIENTES\n2.FUNCIONÁRIOS\n3.CATEGORIAS\n4.FORNECEDORES\n5.PRODUTOS\n6.CAIXA\n--> '))

    if setor == 1:
        return menu_cliente()
    elif setor == 2:
        return menu_funcionario()
    elif setor == 3:
        return menu_categorias()
    elif setor == 4:
        return menu_fornecedores()
    elif setor == 5:
        return menu_produtos()
    elif setor == 6:
        return menu_caixa()

