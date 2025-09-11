# dashboard.py
import matplotlib.pyplot as plt
import re

def dashboard_grafico():
    valores = []
    pedidos = []

    try:
        with open("pedidos.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()

        numero_pedido = 1
        for linha in linhas:
            if linha.startswith("Total:"):
                match = re.search(r"R\$ ?([\d,.]+)", linha)
                if match:
                    valor_str = match.group(1).replace(',', '.')
                    try:
                        valor = float(valor_str)
                        valores.append(valor)
                        pedidos.append(f"Pedido {numero_pedido}")
                        numero_pedido += 1
                    except ValueError:
                        print(f"Valor inválido no pedido {numero_pedido}: {valor_str}")
                else:
                    print(f"Formato inválido na linha: {linha.strip()}")

        if valores:
            plt.figure(figsize=(10,6))
            plt.bar(pedidos, valores, color='skyblue')
            plt.title("Arrecadação por Pedido")
            plt.xlabel("Pedidos")
            plt.ylabel("Valor (R$)")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print("Nenhum pedido registrado ainda.")

    except FileNotFoundError:
        print("Nenhum pedido encontrado ainda.")
