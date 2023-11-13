import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Button

def gerar_plot():
    # Criar um DataFrame com os dados
    df = pd.read_csv('dados.csv', sep=';')

    # Converter a coluna 'data' para o tipo datetime
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')

    # Filtrar por um intervalo de data fixo (por exemplo, de 01/01/1995 a 01/01/2000)
    data_inicial_fixa = pd.to_datetime('01/01/1995', format='%d/%m/%Y')
    data_final_fixa = pd.to_datetime('01/01/2000', format='%d/%m/%Y')
    df_filtrado = df[(df['data'] >= data_inicial_fixa) & (df['data'] <= data_final_fixa)]

    # Calcular a soma da quantidade de veículos e formatar com vírgulas
    soma_veiculos = df_filtrado['valor'].sum()
    soma_veiculos_formatada = "{:,.0f}".format(soma_veiculos)
    
    # Plotar a série temporal
    _, ax = plt.subplots(figsize=(12, 6))  # Usando _ para indicar uma variável não utilizada
    ax.plot(df_filtrado['data'], df_filtrado['valor'], marker='o')
    
    # Adicionar uma etiqueta ao gráfico com a soma da quantidade de veículos
    etiqueta = f"Soma da Quantidade de Veículos: {soma_veiculos_formatada}"
    ax.text(0.5, 0.95, etiqueta, transform=ax.transAxes, ha='right', va='center', bbox=dict(facecolor='white', alpha=0.5))

    plt.title('Produção de Veículos no Brasil ao longo do tempo (Intervalo Fixo)')
    plt.xlabel('Data')
    plt.ylabel('Valor de Produção')
    plt.grid(True)
    plt.show()
    
# 11/04/2020
# 05/05/2023