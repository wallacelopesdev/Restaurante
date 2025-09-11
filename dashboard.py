import matplotlib.pyplot as plt
import re

def dashboard_grafico():
    valores = []
    clientes = []
    pedidos = []

    try:
        with open("pedidos.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()

        numero_pedido = 1
        nome_cliente = None

        for linha in linhas:
            linha = linha.strip()
            if linha.lower().startswith("cliente:"):
                nome_cliente = linha.split(":", 1)[1].strip()
            elif linha.startswith("Total:"):
                match = re.search(r"R\$ ?([\d,.]+)", linha)
                if match:
                    valor_str = match.group(1).replace(',', '.')
                    try:
                        valor = float(valor_str)
                        valores.append(valor)
                        cliente_exibicao = nome_cliente if nome_cliente else "Cliente Desconhecido"
                        clientes.append(cliente_exibicao)
                        pedidos.append(f"Pedido {numero_pedido}")
                        numero_pedido += 1
                        nome_cliente = None
                    except ValueError:
                        print(f"Valor inválido no pedido {numero_pedido}: {valor_str}")
                else:
                    print(f"Formato inválido na linha: {linha}")

        if valores:
            plt.figure(figsize=(12,7))
            barras = plt.bar(clientes, valores, color='skyblue')
            plt.title("Arrecadação por Pedido e Cliente")
            plt.xlabel("Cliente")
            plt.ylabel("Valor (R$)")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()

            for barra in barras:
                altura = barra.get_height()
                plt.text(barra.get_x() + barra.get_width()/2, altura + 1, f"R$ {altura:.2f}", ha='center', va='bottom', fontsize=9)

            plt.show()
        else:
            print("Nenhum pedido registrado ainda.")

    except FileNotFoundError:
        print("Nenhum pedido encontrado ainda.")
