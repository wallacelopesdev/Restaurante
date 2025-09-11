import os
from colorama import Fore, Style, init
from dashboard import dashboard_grafico

# Inicializa o colorama
init(autoreset=True)

NomeDoRestaurante = '𝓢𝓪𝓫𝓸𝓻 𝓑𝓻𝓪𝓼𝓲𝓵𝓮𝓲𝓻𝓸'

# Menus

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
# Funções

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu(menu, titulo):
    print(Fore.YELLOW + f"===== {titulo} =====")
    for codigo, item in menu.items():
        print(f"{codigo}. {item['nome']} - R$ {item['preco']:.2f}")

def mostrar_resumo_pedido(pedido):
    print(Fore.YELLOW + "===== Resumo do seu pedido =====")
    total = 0
    for item in pedido:
        subtotal = item["preco"] * item["qtd"]
        print(f"- {item['nome']} (x{item['qtd']}) - R$ {subtotal:.2f}")
        total += subtotal
    print(f"\nTotal parcial: R$ {total:.2f}")
    return total

def salvar_historico(cliente, telefone, pedido, total, entrega, endereco=None):
    with open("pedidos.txt", "a", encoding="utf-8") as f:
        f.write(f"Cliente: {cliente} | Telefone: {telefone}\n")
        f.write("Itens do pedido:\n")
        for item in pedido:
            f.write(f"- {item['nome']} (x{item['qtd']}) - R$ {item['preco'] * item['qtd']:.2f}\n")
        f.write(f"Total: R$ {total:.2f}\n")
        f.write(f"Entrega: {entrega}\n")
        if endereco:
            f.write(f"Endereço: {endereco}\n")
        f.write("="*30 + "\n\n")

def finalizar_app():
    limpar()
    print(Fore.CYAN + f"Obrigado por usar o aplicativo de pedidos do {NomeDoRestaurante}!\n")
    exit()

# Cadastro inicial

acesso = input("Você deseja acessar o aplicativo de pedidos do restaurante? (s/n): ").strip().lower()
if acesso != 's':
    print("Obrigado! Volte sempre.")
    exit()
else:
    limpar()

cliente = input("Digite seu nome: ").strip()
telefone = input("Digite seu telefone: ").strip()
print(Fore.GREEN + f"\nBem-vindo, {cliente}! Seu número ({telefone}) será usado para contato.\n")

# Pedido

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
        print(Fore.RED + "Opção inválida! Tente novamente.")
        continue

    while True:
        escolha = input("\nDigite o código do produto para adicionar (ou 'voltar' para menu principal): ").strip().upper()
        if escolha.lower() == "voltar":
            limpar()
            break
        try:
            codigo = int(escolha)
            if codigo in menu_atual:
                quantidade = input("Digite a quantidade: ").strip()
                if not quantidade.isdigit() or int(quantidade) <= 0:
                    print(Fore.RED + "Quantidade inválida. Digite um número inteiro positivo.")
                    continue
                quantidade = int(quantidade)
                pedido.append({"nome": menu_atual[codigo]["nome"], "preco": menu_atual[codigo]["preco"], "qtd": quantidade})
                print(Fore.GREEN + f"{menu_atual[codigo]['nome']} (x{quantidade}) adicionado ao pedido.")
            else:
                print(Fore.RED + "Código inválido. Tente novamente.")
        except ValueError:
            print(Fore.RED + "Entrada inválida. Digite um número ou 'voltar'.")

# Resumo do pedido

if not pedido:
    finalizar_app()

limpar()
total = mostrar_resumo_pedido(pedido)

# Remover item com quantidade

remover = input("\nDeseja remover algum item do pedido? (s/n): ").strip().lower()
while remover == "s" and pedido:
    for i, item in enumerate(pedido, 1):
        print(f"{i}. {item['nome']} (x{item['qtd']}) - R$ {item['preco']*item['qtd']:.2f}")
    try:
        excluir = int(input("Digite o número do item que deseja remover: ").strip())
        if 1 <= excluir <= len(pedido):
            item_selecionado = pedido[excluir - 1]
            while True:
                qtd_remover = input(f"Quantas unidades de '{item_selecionado['nome']}' deseja remover? (max {item_selecionado['qtd']}): ").strip()
                if not qtd_remover.isdigit():
                    print(Fore.RED + "Digite um número válido.")
                    continue
                qtd_remover = int(qtd_remover)
                if 1 <= qtd_remover <= item_selecionado['qtd']:
                    break
                else:
                    print(Fore.RED + f"Quantidade inválida. Digite um valor entre 1 e {item_selecionado['qtd']}.")
            # Remove a quantidade solicitada
            item_selecionado['qtd'] -= qtd_remover
            print(Fore.RED + f"Removido {qtd_remover} unidade(s) de {item_selecionado['nome']}.")
            # Se quantidade zerar, remove o item da lista
            if item_selecionado['qtd'] == 0:
                pedido.pop(excluir - 1)
                print(Fore.RED + f"Item {item_selecionado['nome']} removido completamente do pedido.")
            if pedido:
                total = mostrar_resumo_pedido(pedido)
            else:
                print(Fore.RED + "Todos os itens foram removidos do pedido.")
                print(Fore.CYAN + "Encerrando o aplicativo, pois não há itens no pedido.")
                exit()
        else:
            print(Fore.RED + "Número inválido.")
    except ValueError:
        print(Fore.RED + "Entrada inválida.")
    if pedido:
        remover = input("\nDeseja remover outro item? (s/n): ").strip().lower()
    else:
        break

# Cupom de desconto

cupom = input("\nDigite um cupom de desconto (ou Enter para continuar): ").strip().upper()
if cupom == "DESCONTO10":
    total *= 0.9
    print(Fore.GREEN + "✅ Cupom aplicado! 10% de desconto.")
elif cupom == "DESCONTO20":
    total *= 0.8
    print(Fore.GREEN + "✅ Cupom aplicado! 20% de desconto.")
elif cupom != "":
    print(Fore.RED + "Cupom inválido. Nenhum desconto aplicado.")
else:
    print("Nenhum cupom aplicado.")

# Entrega ou Retirada

while True:
    print("\nOpções de recebimento:")
    print("1. Retirar no local")
    print("2. Entrega em casa")
    entrega = input("Escolha 1 ou 2: ").strip()
    if entrega == "1":
        endereco = None
        print(Fore.CYAN + "Seu pedido estará pronto para retirada em 20 minutos.")
        break
    elif entrega == "2":
        endereco = input("Digite seu endereço: ").strip()
        print(Fore.CYAN + f"Seu pedido será entregue em: {endereco}")
        break
    else:
        print(Fore.RED + "Opção inválida. Por favor, escolha 1 ou 2.")

# Tempo estimado

tempo_estimado = 10 + len(pedido) * 5
print(Fore.YELLOW + f"\n⏳ Seu pedido ficará pronto em aproximadamente {tempo_estimado} minutos.")

# Pagamento

print("\nMétodos de pagamento disponíveis:")
metodoDePagamento = ["1. Dinheiro", "2. Cartão de Crédito", "3. Cartão de Débito", "4. Pix"]
print('\n'.join(metodoDePagamento))

print(Fore.GREEN + f"\nTotal final a pagar: R$ {total:.2f}")

metodo_pagamento = input("\nEscolha o método de pagamento (1, 2, 3 ou 4): \n").strip()
if metodo_pagamento == '1':
    print("Você escolheu pagar em Dinheiro.")
elif metodo_pagamento == '2':
    print("Você escolheu pagar com Cartão de Crédito.")
elif metodo_pagamento == '3':
    print("Você escolheu pagar com Cartão de Débito.")
elif metodo_pagamento == '4':
    print("Você escolheu pagar com Pix.")
else:
    print(Fore.RED + "Método de pagamento inválido. Será definido no balcão.")

# Salvar histórico

salvar_historico(cliente, telefone, pedido, total, "Entrega" if entrega == "2" else "Retirada", endereco)

print(Fore.CYAN + "\nUm garçom estará com você em breve para finalizar o pagamento.")
print(Fore.CYAN + f"\nObrigado por visitar o {NomeDoRestaurante}! Volte sempre!")

# Dashboard gráfico

ver_dashboard = input("\nDeseja ver o dashboard de arrecadação? (s/n): ").strip().lower()
if ver_dashboard == 's':
    dashboard_grafico()

