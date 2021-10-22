import shutil
from tkinter import messagebox, filedialog


def carregar_imagens():
    messagebox.showinfo("Etapa 1", "Escolha uma ou mais imagens para adicionar ao diretório")
    imagens = filedialog.askopenfiles()
    messagebox.showinfo("Etapa 2", "Escolha a pasta do Banco de Imagens")
    destino = filedialog.askdirectory()
    shutil.copy(imagens.name,destino)