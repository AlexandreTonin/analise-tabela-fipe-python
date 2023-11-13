from tkinter import Tk, Button
import automaticoxmanual as automaticoxmanual
import carromaiscaroxmarca as carromaiscaroxmarca
import precoxano as precoxano
import precoxtamanhomotor as precoxtamanhomotor
import quantidadexmarca as quantidadexmarca

# Criar a janela principal
janela = Tk()
janela.title("Trabalho Programação para ciência de dados")

# Ajustar o tamanho da janela
largura_janela = 800
altura_janela = 600
janela.geometry(f"{largura_janela}x{altura_janela}")

# Botão para gerar o plot
botao_gerar_plot = Button(janela, text="Carro mais caro de cada marca", command=carromaiscaroxmarca.gerar_plot, bg="#659bb8", fg="#fff")
botao_gerar_plot.pack(pady=5, fill="x")

botao_gerar_plot = Button(janela, text="Preço entre carros automáticos e manuais", command=automaticoxmanual.gerar_plot, bg="#659bb8", fg="#fff")
botao_gerar_plot.pack(pady=5, fill="x")

botao_gerar_plot = Button(janela, text="Quantidade de carro que cada marca possui", command=quantidadexmarca.gerar_plot, bg="#659bb8", fg="#fff")
botao_gerar_plot.pack(pady=5, fill="x")

botao_gerar_plot = Button(janela, text="Preço por ano do modelo dos veículos", command=precoxano.gerar_plot, bg="#659bb8", fg="#fff")
botao_gerar_plot.pack(pady=5, fill="x")

botao_gerar_plot = Button(janela, text="Preço comparado ao tamanho de motores", command=precoxtamanhomotor.gerar_plot, bg="#659bb8", fg="#fff")
botao_gerar_plot.pack(pady=5, fill="x")

# Iniciar o loop principal da interface gráfica
janela.mainloop()

