import pandas as pd
import matplotlib.pyplot as plt

def gerar_plot():
    # Carregando os dados do arquivo CSV
    data = pd.read_csv("dados.csv")

    # Criando um DataFrame com a contagem de carros automáticos e manuais por ano de fabricação
    count_data = data.groupby(['year_model', 'gear']).size().unstack(fill_value=0)

    # Calculando as porcentagens
    count_data['Total'] = count_data['automatic'] + count_data['manual']
    count_data['Porcentagem_Automatico'] = (count_data['automatic'] / count_data['Total']) * 100
    count_data['Porcentagem_Manual'] = (count_data['manual'] / count_data['Total']) * 100

    # Formatando os anos
    count_data.index = count_data.index.astype(int)

    # Criando um gráfico de barras empilhadas
    plt.figure(figsize=(12, 6))
    ax = count_data[['Porcentagem_Automatico', 'Porcentagem_Manual']].plot(kind='bar', stacked=True)

    plt.title('Porcentagem de Carros Automáticos e Manuais por Ano de Fabricação')
    plt.xlabel('Ano de Fabricação')
    plt.ylabel('Porcentagem')
    plt.legend(title='Tipo de Transmissão', loc='upper left')
    plt.show()