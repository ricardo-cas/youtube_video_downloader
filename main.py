from tkinter import *
from pytube import YouTube


# Tela principal
master = Tk() # inicia a instancia do TKinter

master.title("Youtube Downloader") # define o título da janela

master.iconbitmap('.\icone.ico') ## Definindo o ícone do aplicativo

master.minsize(300,300) # definindo o tamanho mínimo da janela
master.maxsize(500,500) # definindo o tamanho maximo da janela




# Labels

Label(master, text="Baixar Vídeos do Youtube", fg="red", font=("Calibri",15)).grid(sticky=N,padx=100,row=0)

Label(master, text="Cole o link do vídeo no campo abaixo para baixar:", font=("Calibri",12)).grid(sticky=N,pady=15,row=1)




master.mainloop() # obrigatório para a execução do programa



# print('Hello World')