import os
import shutil
import tkinter
from operator import itemgetter
from tkinter import messagebox, filedialog
import PIL
import imagehash as imagehash
from PIL import Image



root = tkinter.Tk()
root.wm_withdraw() # this completely hides the root window

def carregar_imagens():
    qnt_image = 0
    messagebox.showinfo("Etapa 1", "Escolha uma ou mais imagens para adicionar ao diretório")
    imagens = filedialog.askopenfiles()
    if len(imagens) > 0:
        messagebox.showinfo("Etapa 2", "Escolha a pasta do Banco de Imagens")
        destino = filedialog.askdirectory()
        if len(destino) > 0:
            for i in imagens:
                testa_figura = verifica_jpg(i.name)
                testa_image = image_corrompida(i.name)
                if testa_figura and testa_image:
                    shutil.copy(i.name, destino)
                    i.close()
                    qnt_image +=1

            print("Foram carregadas : ", qnt_image, " imagens")


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

    except PIL.UnidentifiedImageError:
        i = False
        print("A primeira imagem está corrompida")
    if i:
        messagebox.showinfo("Etapa 2", "Escolha a segunda imagem para comparação")
        imagem_B = filedialog.askopenfile()
        try:
            imagem_Y = PIL.Image.open(imagem_B.name)
            h2 = imagehash.phash(imagem_Y)

            resultado = 100 - ((h1 - h2) / len(h2.hash) ** 2 * 100)
            print("A imagem  em", imagem_A.name, "\ntem ", resultado, "% de similaridade com a imagem ", imagem_B.name)
        except PIL.UnidentifiedImageError:
            print("A segunda imagem está corrompida")



def achar_similaridade():
    n=3
    list_dic = {}
    dic_hash = {}
    dic_mapeado = {}
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
                    f = PIL.Image.open(imagens+ "/" + file)
                    h = imagehash.phash(f)
                    dic_hash[file]=h
                except PIL.UnidentifiedImageError:
                    print("Esta imagem ", file, " está corrompida e será ignorada")

        for i in dic_hash:
            resultado = 100- ((h1 - dic_hash[i]) / len(dic_hash[i].hash) ** 2*100)
            list_dic[i] = resultado
        dic_mapeado = dict(sorted(list_dic.items(), key=itemgetter(1), reverse=True)[:n])
        print("\nOs ",n," maiores valores são: " , dic_mapeado)


def verifica_jpg(str):
    st = str.split(".")
    if st[-1] == "jpg":
        return True
    else:
        print("A imagem ",str," não foi carregada")
        print("Só são aceitas imagens jpg")

def image_corrompida(str):
    flag = True
    try:
        imagem_X = PIL.Image.open(str)

    except PIL.UnidentifiedImageError:
        flag = False

    if flag:
        return True
    else:
        print(str, " Não pode ser carregada, arquivo corrompido")

