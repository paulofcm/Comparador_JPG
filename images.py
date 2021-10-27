import os
import pickle
import shutil
import tkinter
from operator import itemgetter
from tkinter import messagebox, filedialog
import PIL
import imagehash as imagehash
from PIL import Image

import utils

root = tkinter.Tk()
root.wm_withdraw() # this completely hides the root window

def load_images():
    images = utils.images_to_load("Load images", "Select one or more images to load")
    path = utils.select_path("Load path", "Select image bank directory")
    if images != None and path != None:
        for image in images:
            is_jpg = utils.verify_jpg(image.name)
            is_ok = utils.verify_image(image.name)
            if is_jpg and is_ok:
                image.close()
                shutil.copy(image.name,path)

def del_images():
    images = utils.images_to_load()
    if images != None:
        for image in images:
            image.close()
            os.remove(image.name)

def create_db_image_hash():
    images = utils.images_to_load("Load images", "Select files from the image bank")
    path = utils.select_path("Database directory", "Select the database directory")
    dic_image_hash = {}
    file_pkl_path = path+"//DBImageHash.pkl"
    file = open(file_pkl_path, "wb")
    for image in images:
        imagem_to_hash = PIL.Image.open(image.name)
        imagem_hash = imagehash.phash(imagem_to_hash)
        print(imagem_hash)
        dic_image_hash[image.name] = imagem_hash
    pickle.dump(dic_image_hash, file)
    file.close()
    print("File.pkl complete", dic_image_hash.keys())
    dic_hash = {}
    print("Dic dic_hash empty", dic_image_hash.keys())


def find_similar():
    Percent = 100
    dicimages_to_compare = {}
    dic_hash = {}
    list_dic_result = {}
    number_of_result = 3
    path = utils.select_path("DB Function", "Select the DB dir")
    file_pkl_file = path + "//DBImageHash.pkl"
    file = open(file_pkl_file, "rb")
    dic_hash = pickle.load(file)
    file.close()
    image_select = utils.image_to_load("Select Image", "Select 1 image to compare")
    image_to_hash = PIL.Image.open(image_select.name)
    image_hash = imagehash.phash(image_to_hash)
    for image in dic_hash:
        result = Percent - ((image_hash - dic_hash[image]) / len(dic_hash[image].hash) ** 2 * Percent)
        list_dic_result[image] = result
        dic_maped = dict(sorted(list_dic_result.items(), key=itemgetter(1), reverse=True)[:number_of_result])
    print("\nThe ", number_of_result, " greater similarity with", image_select.name, "is(are):\n")
    for image in dic_maped:
        print(image, " ", dic_maped[image], "%")
