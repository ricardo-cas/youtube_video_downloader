from tkinter import *
from pytube import YouTube


# Tela principal
master = Tk() # inicia a instancia do TKinter

master.title("Youtube Downloader") # define o título da janela

master.iconbitmap('.\icone.ico') ## Definindo o ícone do aplicativo

# Labels

Label(master, text="Download Converter Youtube", fg="red", font=("Calibri",15)).grid(sticky=N,padx=100,row=0)

Label(master, text="Cole o link do vídeo no campo abaixo para baixar:", fg="blue", font=("Calibri",12)).grid(sticky=N,pady=15,row=1)




master.mainloop() # obrigatório para a execução do programa



# print('Hello World')