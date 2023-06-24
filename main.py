import csv
import os

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

def cadastrar_cliente():
    senha = input("Digite a senha do novo cliente: ")
    nome = input("Digite o nome do novo cliente: ")
    cpf = input("Digite o CPF do novo cliente: ")
    celular = input("Digite o número de celular do novo cliente: ")
    clientes[senha] = {"nome": nome, "cpf": cpf, "celular": celular}
    salvar_clientes(clientes)
    print("Novo cliente cadastrado com sucesso!")


carrinho = []
produtos = carregar_produtos()
clientes = carregar_clientes()

while True:
    print("Menu:")
    print("1. Ver Estoque")
    print("2. Adicionar Produto ao Carrinho")
    print("3. Ver Carrinho")
    print("4. Finalizar Compra")
    print("5. Cadastrar Cliente")
    print("6. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        exibir_estoque(produtos)

    elif opcao == "2":
        adicionar_ao_carrinho(produtos, carrinho)

    elif opcao == "3":
        exibir_carrinho(carrinho)

    elif opcao == "4":
        finalizar_compra(carrinho)

    elif opcao == "5":
        cadastrar_cliente()

    elif opcao == "6":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Por favor, digite um número válido.")
