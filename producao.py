import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Button

def gerar_plott():
    # Criar um DataFrame com os dados
    df = pd.read_csv('dados.csv', sep=';')

    # Converter a coluna 'data' para o tipo datetime
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    
    # Calcular a soma da quantidade de veículos e formatar com vírgulas
    soma_veiculos = df['valor'].sum()
    soma_veiculos_formatada = "{:,.0f}".format(soma_veiculos)
    
    # Plotar a série temporal
    _, ax = plt.subplots(figsize=(12, 6))  # Usando _ para indicar uma variável não utilizada
    ax.plot(df['data'], df['valor'], marker='o')
    
    # Adicionar uma etiqueta ao gráfico com a soma da quantidade de veículos
    etiqueta = f"Soma da Quantidade de Veículos: {soma_veiculos_formatada}"
    ax.text(0.5, 0.95, etiqueta, transform=ax.transAxes, ha='right', va='center', bbox=dict(facecolor='white', alpha=0.5))

    plt.title('Produção de Veículos no Brasil ao longo do tempo (Intervalo Fixo)')
    plt.xlabel('Data')
    plt.ylabel('Valor de Produção')
    plt.grid(True)
    plt.show()