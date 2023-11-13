import pandas as pd
import matplotlib.pyplot as plt

def gerar_plot():
    # Carregando os dados do arquivo CSV
    data = pd.read_csv("dados.csv")

    # Calculando a média dos preços por tamanho de motor
    average_prices = data.groupby('engine_size')['avg_price_brl'].mean()

    # Criando um gráfico de barras
    plt.figure(figsize=(12, 6))
    average_prices.plot(kind='bar', color='skyblue')
    plt.title('Média de Preço por Tamanho do Motor')
    plt.xlabel('Tamanho do Motor')
    plt.ylabel('Média de Preço (BRL)')

    # Formatando os valores do eixo y como inteiros
    plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}"))

    plt.show()