from tkinter import *

janela = Tk() #inicia uma janela


janela.title("Apple") #Titulo da janela
#Define altura, largura, posição
janela.geometry("640x480+350+150")
# Muda o icone da janela
janela.iconbitmap(r'C:\Users\Família\Documents\Projetos Py\ImagemIco\apple.ico')
# cor de fundo da janela
janela['bg'] = "white" 

imag = PhotoImage(file="imagens/logo-apple.png")
varLab = Label(janela, image=imag)
varLab.place(y = 83 , x = 180)


janela.mainloop() #loop da janela, pra mante-lá










