import pandas as pd
import matplotlib.pyplot as plt

def gerar_plot():
    # Leitura do CSV
    df = pd.read_csv('dados.csv')

    # Remover duplicatas considerando apenas marca e modelo
    unique_cars = df[['brand', 'model']].drop_duplicates()

    # Contagem da quantidade de carros únicos por marca
    count_by_brand = unique_cars['brand'].value_counts()

    # Exibir a contagem
    print("Quantidade de carros únicos por marca:")
    print(count_by_brand)

    # Plotar gráfico de barras
    plt.figure(figsize=(12, 6))
    count_by_brand.plot(kind='bar', color='skyblue')
    plt.title('Quantidade de carros únicos por marca')
    plt.xlabel('Marca')
    plt.ylabel('Quantidade de Carros Únicos')

    # Adicionar rótulos nas barras
    for i, v in enumerate(count_by_brand):
        plt.text(i, v + 0.1, str(v), ha='center', va='bottom', fontsize=8)

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
