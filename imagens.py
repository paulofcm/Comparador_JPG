import os
import shutil
import tkinter
from tkinter import messagebox, filedialog
import PIL
import imagehash as imagehash
from PIL import Image

root = tkinter.Tk()
root.wm_withdraw() # this completely hides the root window

def carregar_imagens():
    messagebox.showinfo("Etapa 1", "Escolha uma ou mais imagens para adicionar ao diretório")
    imagens = filedialog.askopenfiles()
    if len(imagens) > 0:
        messagebox.showinfo("Etapa 2", "Escolha a pasta do Banco de Imagens")
        destino = filedialog.askdirectory()
        if len(destino) > 0:
            for i in imagens:
                i.close()
                shutil.copy(i.name,destino)
            print(len(imagens))

def deletar_imagens():
    messagebox.showinfo("Etapa 1", "Escolha uma ou mais imagens para deletar")
    imagens = filedialog.askopenfiles()
    if len(imagens) > 0:
        for i in imagens:
            i.close()
            os.remove(i.name)

def comparar_imagens():
    messagebox.showinfo("Etapa 1", "Escolha a imagem para ser comparada")
    imagem_A = filedialog.askopenfile()
    i = True
    try:
        imagem_X = PIL.Image.open(imagem_A.name)
        h1 = imagehash.phash(imagem_X)
        print(h1)
    except PIL.UnidentifiedImageError:
        i = False
        print("A primeira imagem está corrompida")
    if i:
        messagebox.showinfo("Etapa 2", "Escolha a segunda imagem para comparação")
        imagem_B = filedialog.askopenfile()
        try:
            imagem_Y = PIL.Image.open(imagem_B.name)
            h2 = imagehash.phash(imagem_Y)
            print(h2)
        except PIL.UnidentifiedImageError:
            print("A segunda imagem está corrompida")
