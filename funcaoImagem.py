import os
import shutil
from tkinter import messagebox, filedialog

import PIL
import imagehash


def verifica_jpg(str):
    st = str.split(".")
    if st[-1] == "jpg":
        return True
    else:
        print("A imagem ",str," não foi carregada")
        print("Só são aceitas imagens jpg")

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

def carregar_imagens():
    messagebox.showinfo("Etapa 1", "Escolha uma ou mais imagens para adicionar ao diretório")
    imagens = filedialog.askopenfiles()
    for i in imagens:
        try:
            imagem_X = PIL.Image.open(i.name)
            h1 = imagehash.phash(imagem_X)
            print(h1)
        except PIL.UnidentifiedImageError:
            i = False
            print("A imagem", i, "está corrompida")
        if len(imagens) > 0:
            messagebox.showinfo("Etapa 2", "Escolha a pasta do Banco de Imagens")
            destino = filedialog.askdirectory()
            if len(destino) > 0:
                for i in imagens:
                    testa_figura = verifica_jpg(i.name)
                    if testa_figura:
                        i.close()
                        shutil.copy(i.name,destino)
                print("Foram carregadas : ",len(imagens)," imagens")

def carregar_imagens():
    messagebox.showinfo("Etapa 1", "Escolha uma ou mais imagens para adicionar ao diretório")
    imagens = filedialog.askopenfiles()
    if len(imagens) > 0:
        messagebox.showinfo("Etapa 2", "Escolha a pasta do Banco de Imagens")
        destino = filedialog.askdirectory()
        if len(destino) > 0:
            for i in imagens:
                testa_figura = verifica_jpg(i.name)
                if testa_figura:
                    i.close()
                    shutil.copy(i.name, destino)
            print("Foram carregadas : ", len(imagens), " imagens")

def achar_similaridade():
    dic_hash = {}
    messagebox.showinfo("Etapa 1", "Escolha a imagem para ser comparada")
    imagem_A = filedialog.askopenfile()
    str = imagem_A.name
    sp = str.split("/")
    nome_da_imagem = sp[-1]
    i = verifica_jpg(imagem_A.name)
    if i:
        try:
            imagem_X = PIL.Image.open(imagem_A.name)
            h1 = imagehash.phash(imagem_X)
        except PIL.UnidentifiedImageError:
            i = False
            print("A imagem ", imagem_X, " esta corrompida")
        if i:
            messagebox.showinfo("Etapa 2", "Escolha o banco de imagens  para comparação")
            imagens = filedialog.askdirectory()
            for file in os.listdir(imagens):
                try:
                    f = PIL.Image.open(imagens+ "\\" + file)
                    h = imagehash.phash(f)
                    dic_hash[file]=h
                except PIL.UnidentifiedImageError:
                    print("Esta imagem ", file, " está corrompida e será ignorada")
        maior = 0
        indice = ""
        for i in dic_hash:
            resultado = 100- ((h1 - dic_hash[i]) / len(dic_hash[i].hash) ** 2*100)
            if resultado > maior:
                maior = resultado
                indice = i
        #imagem_X.show()
        print("A imagem  em",imagem_A.name,"\ntem ",maior,"% de similaridade com a imagem ", indice)
        print("A imagem ", nome_da_imagem, "tem ", maior, "% de similaridade com a imagem ", indice)
