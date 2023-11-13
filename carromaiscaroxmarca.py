import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import mplcursors


def gerar_plot():
    # Leitura do CSV
    df = pd.read_csv("dados.csv")

    # Ordenar o DataFrame pelo preço médio em ordem decrescente
    df_sorted = df.sort_values(by="avg_price_brl", ascending=False)

    # Selecionar o carro mais caro de cada marca
    top_cars_by_brand = df_sorted.groupby("brand").first().reset_index()

    # Selecionar o carro mais caro de todos
    carro_mais_caro = df_sorted.iloc[0]

    # Selecionar o carro mais barato de todos
    carro_mais_barato = df_sorted.iloc[-1]

    # Exibir o resultado
    print("Carro mais caro de cada marca:")
    print(top_cars_by_brand[["brand", "model", "avg_price_brl"]])
    print("\nCarro mais caro de todos:")
    print(carro_mais_caro[["brand", "model", "avg_price_brl"]])
    print("\nCarro mais barato de todos:")
    print(carro_mais_barato[["brand", "model", "avg_price_brl"]])

    # Função para formatar o eixo y em milhões
    def millions_formatter(x, pos):
        return f"R${x/1e6:.1f}M"

    # Plotar gráfico de barras com formatação do eixo y
    plt.figure(figsize=(12, 6))
    bars = plt.bar(
        top_cars_by_brand["brand"], top_cars_by_brand["avg_price_brl"], color="skyblue"
    )
    plt.title("Carro mais caro de cada marca")
    plt.xlabel("Marca")
    plt.ylabel("Preço Médio (BRL)")
    plt.xticks(rotation=45, ha="right")

    # Adicionar o nome do modelo somente quando o mouse está sobre a barra
    mplcursors.cursor(hover=True).connect(
        "add",
        lambda sel: sel.annotation.set_text(
            top_cars_by_brand["model"][sel.target.index]
        ),
    )

    # Adicionar etiquetas para o carro mais caro e mais barato de todos
    plt.text(
        -0.2,
        carro_mais_caro["avg_price_brl"] + 0.05e6,
        f"Carro mais caro:\n{carro_mais_caro['brand']} {carro_mais_caro['model']}\nR${carro_mais_caro['avg_price_brl']:,}",
        ha="center",
        color="black",
        fontsize=8,
    )
    plt.text(
        -0.2,
        carro_mais_barato["avg_price_brl"] - 0.15e6,
        f"Carro mais barato:\n{carro_mais_barato['brand']} {carro_mais_barato['model']}\nR${carro_mais_barato['avg_price_brl']:,}",
        ha="center",
        color="black",
        fontsize=8,
    )

    # Aplicar a formatação do eixo y
    formatter = FuncFormatter(millions_formatter)
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.tight_layout()
    plt.show()
