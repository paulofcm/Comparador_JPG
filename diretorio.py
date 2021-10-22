import os
from tkinter import filedialog, messagebox

def criar_diretorio():
    messagebox.showinfo("Etapa 1","Escolha o local para criar uma pasta")
    destino = filedialog.askdirectory()
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

    try:
        os.rmdir(diretorio)
    except FileExistsError:
        pass