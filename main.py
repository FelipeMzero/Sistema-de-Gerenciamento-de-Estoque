import csv
import os
from datetime import datetime

def exibir_estoque(produtos):
    print("Estoque:")
    for produto in produtos:
        print(f"Produto: {produto['nome'].upper()} | Preço: R$ {produto['preco']} | Estoque: {produto['estoque']} unidades")
    print()

def adicionar_ao_carrinho(produtos, carrinho):
    nome_produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ").upper()
    quantidade = int(input("Digite a quantidade desejada: "))

    for produto in produtos:
        if produto['nome'].upper() == nome_produto:
            if produto['estoque'] >= quantidade:
                produto['estoque'] -= quantidade
                item_carrinho = {"nome": produto['nome'], "preco": produto['preco'], "quantidade": quantidade}
                carrinho.append(item_carrinho)
                print(f"{quantidade} unidades de {produto['nome'].upper()} foram adicionadas ao carrinho.")
            else:
                print(f"Desculpe, não há estoque suficiente de {produto['nome'].upper()}.")
            break
    else:
        print(f"O produto {nome_produto} não foi encontrado.")

def exibir_carrinho(carrinho):
    if len(carrinho) == 0:
        print("O carrinho está vazio.")
    else:
        print("Carrinho:")
        for item in carrinho:
            print(f"Produto: {item['nome']} | Preço: R$ {item['preco']} | Quantidade: {item['quantidade']} unidades")
        print()

def finalizar_compra(carrinho, clientes):
    if len(carrinho) == 0:
        print("O carrinho está vazio. Não é possível finalizar a compra.")
    else:
        valor_total = 0
        for item in carrinho:
            valor_total += item['preco'] * item['quantidade']

        desconto = 0
        senha = input("Digite sua senha (ou deixe em branco para não aplicar desconto): ")
        if senha:
            if senha in clientes:
                desconto = valor_total * 0.05
                valor_total -= desconto
                print(f"Desconto aplicado: R$ {desconto:.2f}")
            else:
                print("Senha inválida. Desconto não aplicado.")

        print("Finalizando compra...")
        print("Itens no carrinho:")
        for item in carrinho:
            print(f"Produto: {item['nome']} | Preço: R$ {item['preco']} | Quantidade: {item['quantidade']} unidades")
        print(f"Valor total a pagar: R$ {valor_total:.2f}")

        # Registrar a venda no histórico
        registrar_venda(carrinho, valor_total)

        carrinho.clear()
        print("Compra realizada com sucesso! O carrinho foi esvaziado.")

def registrar_venda(carrinho, valor_total):
    file_path = os.path.join('data', f'venda_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Itens no carrinho:\n")
        for item in carrinho:
            file.write(f"Produto: {item['nome']} | Preço: R$ {item['preco']} | Quantidade: {item['quantidade']} unidades\n")
        file.write(f"Valor total a pagar: R$ {valor_total:.2f}\n")

def carregar_produtos():
    produtos = []
    file_path = os.path.join('data', 'produtos.csv')
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produto = {"nome": row['nome'], "preco": float(row['preco']), "estoque": int(row['estoque'])}
            produtos.append(produto)
    return produtos

def salvar_produtos(produtos):
    file_path = os.path.join('data', 'produtos.csv')
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['nome', 'preco', 'estoque']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)

def carregar_clientes():
    clientes = {}
    file_path = os.path.join('data', 'clientes.csv')
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            senha = row['senha']
            nome = row['nome']
            cpf = row['cpf']
            celular = row['celular']
            clientes[senha] = {"nome": nome, "cpf": cpf, "celular": celular}
    return clientes

def salvar_clientes(clientes):
    file_path = os.path.join('data', 'clientes.csv')
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['senha', 'nome', 'cpf', 'celular']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for senha, dados_cliente in clientes.items():
            writer.writerow({'senha': senha, 'nome': dados_cliente['nome'], 'cpf': dados_cliente['cpf'], 'celular': dados_cliente['celular']})

def cadastrar_cliente(clientes):
    senha = input("Digite a senha do novo cliente: ")
    nome = input("Digite o nome do novo cliente: ")
    cpf = input("Digite o CPF do novo cliente: ")
    celular = input("Digite o número de celular do novo cliente: ")
    clientes[senha] = {"nome": nome, "cpf": cpf, "celular": celular}
    salvar_clientes(clientes)
    print("Novo cliente cadastrado com sucesso!")

def exibir_historico_vendas():
    directory = os.path.join('data', 'historico_vendas')
    if os.path.exists(directory):
        files = os.listdir(directory)
        if files:
            print("Histórico de Vendas:")
            for file in files:
                file_path = os.path.join(directory, file)
                with open(file_path, 'r', encoding='utf-8') as file:
                    print(file.read())
        else:
            print("Nenhum histórico de vendas encontrado.")
    else:
        print("Nenhum histórico de vendas encontrado.")

def remover_do_carrinho(carrinho):
    if len(carrinho) == 0:
        print("O carrinho está vazio.")
    else:
        nome_produto = input("Digite o nome do produto que deseja remover do carrinho: ").upper()
        quantidade = int(input("Digite a quantidade que deseja remover: "))
        for item in carrinho:
            if item['nome'].upper() == nome_produto:
                if item['quantidade'] > quantidade:
                    item['quantidade'] -= quantidade
                    print(f"{quantidade} unidades de {item['nome'].upper()} foram removidas do carrinho.")
                elif item['quantidade'] == quantidade:
                    carrinho.remove(item)
                    print(f"Todas as unidades de {item['nome'].upper()} foram removidas do carrinho.")
                else:
                    print(f"A quantidade a ser removida é maior do que a quantidade disponível no carrinho para {item['nome'].upper()}.")
                break
        else:
            print(f"O produto {nome_produto} não foi encontrado no carrinho.")

carrinho = []
produtos = carregar_produtos()
clientes = carregar_clientes()



def finalizar_compra(carrinho):
    if len(carrinho) == 0:
        print("O carrinho está vazio. Não é possível finalizar a compra.")
    else:
        valor_total = 0
        for item in carrinho:
            valor_total += item['preco'] * item['quantidade']

        desconto = 0
        senha = input("Digite sua senha (ou deixe em branco para não aplicar desconto): ")
        if senha:
            # Aqui você pode adicionar a lógica de autenticação do usuário, caso necessário
            desconto = valor_total * 0.05
            valor_total -= desconto

        print("Finalizando compra...")
        print("Itens no carrinho:")
        for item in carrinho:
            print(f"Produto: {item['nome']} | Preço: R$ {item['preco']} | Quantidade: {item['quantidade']} unidades")
        print(f"Valor total a pagar: R$ {valor_total:.2f}")
        if desconto > 0:
            print(f"Desconto aplicado: R$ {desconto:.2f}")

        carrinho.clear()
        print("Compra realizada com sucesso! O carrinho foi esvaziado.")

        # Registrar a venda no arquivo de histórico
        registrar_venda(valor_total, datetime.now(), carrinho)

def registrar_venda(valor_total, data, carrinho):
    venda = f"Venda realizada em {data.strftime('%Y-%m-%d %H:%M:%S')}:\n"
    for item in carrinho:
        venda += f"Produto: {item['nome']} | Preço: R$ {item['preco']} | Quantidade: {item['quantidade']} unidades\n"
    venda += f"Valor total: R$ {valor_total:.2f}\n\n"

    file_path = os.path.join('data', f"venda_{data.strftime('%Y%m%d%H%M%S')}.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(venda)

while True:
    print("======== LOJA DE INFORMÁTICA ========")
    print("1 - Exibir Estoque")
    print("2 - Adicionar ao Carrinho")
    print("3 - Exibir Carrinho")
    print("4 - Finalizar Compra")
    print("5 - Cadastrar Cliente")
    print("6 - Exibir Histórico de Vendas")
    print("7 - Remover do Carrinho")
    print("0 - Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        exibir_estoque(produtos)
    elif opcao == "2":
        adicionar_ao_carrinho(produtos, carrinho)
    elif opcao == "3":
        exibir_carrinho(carrinho)
    elif opcao == "4":
        finalizar_compra(carrinho)
    elif opcao == "5":
        cadastrar_cliente(clientes)
    elif opcao == "6":
        exibir_historico_vendas()
    elif opcao == "7":
        remover_do_carrinho(carrinho)
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Digite novamente.")

salvar_produtos(produtos)
