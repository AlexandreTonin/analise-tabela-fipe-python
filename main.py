import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Button
import producao as prod
import covid as covid

# Criar a janela principal
janela = Tk()
janela.title("Trabalho Programação para ciência de dados")

# Ajustar o tamanho da janela
largura_janela = 800
altura_janela = 600
janela.geometry(f"{largura_janela}x{altura_janela}")

# Botão para gerar o plot
botao_gerar_plot = Button(janela, text="Produção de veículos ao longo do tempo", command=prod.gerar_plott, bg="#659bb8", fg="#fff")
botao_gerar_plot.pack(pady=5, fill="x")

botao_gerar_plot = Button(janela, text="Produção de veículos durante o período de pandemia (COVID-19)", command=covid.gerar_plot, bg="#659bb8", fg="#fff")
botao_gerar_plot.pack(pady=5, fill="x")

# Iniciar o loop principal da interface gráfica
janela.mainloop()

