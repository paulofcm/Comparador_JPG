import os
import tkinter
from tkinter import filedialog, messagebox

root = tkinter.Tk()
root.wm_withdraw() # this completely hides the root window

def criar_diretorio():
    messagebox.showinfo("Etapa 1","Escolha o local para criar uma pasta")
    destino = filedialog.askdirectory()
    if len(destino) > 0:
        messagebox.showinfo("Etapa 2","Digite no terminal o nome da pasta")
        pasta_nome = input("Qual o nome da Pasta : ").strip()
        pasta_a_criar = (destino+"//"+pasta_nome)

        try:
            os.mkdir(pasta_a_criar)
        except FileExistsError:
            print("JÁ EXISTE ", pasta_a_criar)


def deletar_diretorio():
    messagebox.showinfo("Etapa 1", "Que diretorio deseja deletar?")
    diretorio = filedialog.askdirectory()
    if len(diretorio) > 0:

        try:
            os.rmdir(diretorio)
        except FileExistsError:
            pass