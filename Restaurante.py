import os







NomeDoRestaurante = "Sabor Brasileiro" 


acesso = input("Você deseja acessar o aplicativo de pedidos do restaurante? (s/n): ").strip().lower()
if acesso != 's':
    print("Obrigado! Volte sempre.")
    exit()
else:
    os.system('cls')





# Produtos 
produtos = { 1: {"nome": "Feijoada 500g", "preco": 25.00}, 
            2: {"nome": "Churrasco No Prato 250g", "preco": 30.00}, 
            3: {"nome": "Moqueca 500g", "preco": 28.00}, 
            4: {"nome": "Tropeiro 450g", "preco": 27.00}, 
            5: {"nome": "Figado Acebolado 350g", "preco": 18.00}, 
            6: {"nome": "Cerveja", "preco": 11.00}, 
            7: {"nome": "Caipirinha", "preco": 8.00},
            8: {"nome": "Martini", "preco": 16.00}, 
            9: {"nome": "Vinho", "preco": 32.00}, 
            10: {"nome": "Whisky", "preco": 45.00} } 
#menu
menu = produtos 
print(f"Bem-vindo ao {NomeDoRestaurante}!") 
print("Aqui está o nosso menu:") 
for codigo, info in menu.items(): 
    print(f"{codigo}. {info['nome']} - R$ {info['preco']:.2f}") 

# Pedido 
pedido = [] 
while True: 
    escolha = input("Digite o código do produto que deseja adicionar ao pedido (ou 'sair' para finalizar): ") 
    if escolha.lower() == 'sair': 
        break 
    try: 
        codigo = int(escolha) 
        if codigo in produtos: 
            pedido.append(produtos[codigo]) 
            print(f"{produtos[codigo]['nome']} adicionado ao pedido.") 
        else: 
            print("Código inválido. Tente novamente.") 
    except ValueError: 
        print("Entrada inválida. Por favor, digite um número ou 'sair'.") 

def finalizar_app(): 
    os.system('cls')
    print("Obrigado por usar o aplicativo de pedidos do Sabor Brasileiro!\n") 
    exit()

# Resumo do pedido 
if pedido: 
    print("\nResumo do seu pedido:") 
    total = 0 
    for item in pedido: 
        print(f"- {item['nome']} - R$ {item['preco']:.2f}") 
        total += item['preco'] 
    print(f"Total a pagar: R$ {total:.2f}") 
else: 
    finalizar_app() 

#metodo de pagamento 
print("\nMétodos de pagamento disponíveis:") 
metodoDePagamento = ["1. Dinheiro", "2. Cartão de Crédito", "3. Cartão de Débito", "4. Pix"]
print('\n'.join(metodoDePagamento))


metodo_pagamento = input("Escolha o método de pagamento (1, 2, 3 ou 4): ") 
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

print("\nUm garçom estará com você em breve para finalizar o pagamento.") 
print("\nObrigado por visitar o Sabor Brasileiro! Volte sempre!")