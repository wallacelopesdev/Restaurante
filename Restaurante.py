import os

NomeDoRestaurante = "Sabor Brasileiro"

# ==============================
# Menus
# ==============================
menuDeComidas = {
    1: {"nome": "Feijoada 500g", "preco": 25.00},
    2: {"nome": "Churrasco No Prato 250g", "preco": 30.00},
    3: {"nome": "Moqueca 500g", "preco": 28.00},
    4: {"nome": "Tropeiro 450g", "preco": 27.00},
    5: {"nome": "Fígado Acebolado 350g", "preco": 18.00}
}

menuDeBebidas = {
    1: {"nome": "Cerveja", "preco": 11.00},
    2: {"nome": "Caipirinha", "preco": 8.00},
    3: {"nome": "Martini", "preco": 16.00},
    4: {"nome": "Vinho", "preco": 32.00},
    5: {"nome": "Whisky", "preco": 45.00}
}

# ==============================
# Funções
# ==============================
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu(menu, titulo):
    print(f"===== {titulo} =====")
    for codigo, item in menu.items():
        print(f"{codigo}. {item['nome']} - R$ {item['preco']:.2f}")

def finalizar_app():
    limpar()
    print("Obrigado por usar o aplicativo de pedidos do Sabor Brasileiro!\n")
    exit()

# ==============================
# Acesso inicial
# ==============================
acesso = input("Você deseja acessar o aplicativo de pedidos do restaurante? (s/n): ").strip().lower()
if acesso != 's':
    print("Obrigado! Volte sempre.")
    exit()
else:
    limpar()

# ==============================
# Pedido
# ==============================
pedido = []

while True:
    print("Qual menu você deseja acessar?")
    print("1. Comidas")
    print("2. Bebidas")
    print("3. Finalizar Pedido")
    escolha_menu = input("Digite 1, 2 ou 3: ").strip()

    limpar()

    if escolha_menu == "1":
        mostrar_menu(menuDeComidas, "Menu de Comidas")
        menu_atual = menuDeComidas

    elif escolha_menu == "2":
        mostrar_menu(menuDeBebidas, "Menu de Bebidas")
        menu_atual = menuDeBebidas

    elif escolha_menu == "3":
        break

    else:
        print("Opção inválida! Tente novamente.")
        continue

    while True:
        escolha = input("\nDigite o código do produto para adicionar (ou 'voltar' para menu principal): ")
        if escolha.lower() == "voltar":
            limpar()
            break
        try:
            codigo = int(escolha)
            if codigo in menu_atual:
                pedido.append(menu_atual[codigo])
                print(f"{menu_atual[codigo]['nome']} adicionado ao pedido.")
            else:
                print("Código inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'voltar'.")

# ==============================
# Resumo do pedido
# ==============================
if pedido:
    limpar()
    print("===== Resumo do seu pedido =====")
    total = 0
    for item in pedido:
        print(f"- {item['nome']} - R$ {item['preco']:.2f}")
        total += item['preco']
    print(f"\nTotal a pagar: R$ {total:.2f}")
else:
    finalizar_app()

# ==============================
# Pagamento
# ==============================
print("\nMétodos de pagamento disponíveis:")
metodoDePagamento = ["1. Dinheiro", "2. Cartão de Crédito", "3. Cartão de Débito", "4. Pix"]
print('\n'.join(metodoDePagamento))

metodo_pagamento = input("\nEscolha o método de pagamento (1, 2, 3 ou 4): ").strip()
if metodo_pagamento == '1':
    print("Você escolheu pagar em Dinheiro.")
elif metodo_pagamento == '2':
    print("Você escolheu pagar com Cartão de Crédito.")
elif metodo_pagamento == '3':
    print("Você escolheu pagar com Cartão de Débito.")
elif metodo_pagamento == '4':
    print("Você escolheu pagar com Pix.")
else:
    print("Método de pagamento inválido. Por favor, reinicie o pedido.")
os.system("cls")
print("\nUm garçom estará com você em breve para finalizar o pagamento.")
print("\nObrigado por visitar o Sabor Brasileiro! Volte sempre!")
