produtos = [
    {"nome": "Placa de Vídeo", "preco": 1500.00, "estoque": 10},
    {"nome": "Memória RAM", "preco": 300.00, "estoque": 20},
    {"nome": "HD Externo", "preco": 250.00, "estoque": 5},
    # Adicione mais produtos conforme necessário
]

def mostrar_estoque():
    print("Estoque disponível:")
    for produto in produtos:
        print(f"Produto: {produto['nome']} | Preço: R$ {produto['preco']} | Estoque: {produto['estoque']} unidades")

def comprar_produto():
    nome_produto = input("Digite o nome do produto que deseja comprar: ")
    quantidade = int(input("Digite a quantidade desejada: "))

    for produto in produtos:
        if produto['nome'] == nome_produto:
            if produto['estoque'] >= quantidade:
                produto['estoque'] -= quantidade
                print(f"{quantidade} unidades de {produto['nome']} foram compradas com sucesso!")
            else:
                print(f"Desculpe, não há estoque suficiente de {produto['nome']}.")

            return

    print(f"O produto {nome_produto} não foi encontrado.")

while True:
    print("\n----- MENU -----")
    print("1. Ver estoque")
    print("2. Comprar produto")
    print("3. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        mostrar_estoque()
    elif opcao == "2":
        comprar_produto()
    elif opcao == "3":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
