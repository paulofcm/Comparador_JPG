import os
import tkinter
from tkinter import filedialog, messagebox

import utils

root = tkinter.Tk()
root.wm_withdraw() # this completely hides the root window


def create_dir():
    #str1 = "Creat a dir"
    #str2 = "Select local to create dir"
    path = utils.select_path("Creat a dir","Select local to create dir")
    if path != None:
        messagebox.showinfo("Diretory", "Enter the name of the new directory into the terminal.")
        new_path = input("Path name : ").strip()
        if len(new_path)>0:
            path_to_create = (path+"//"+new_path)
            try:
                os.mkdir(path_to_create)
                print("Path created")
            except FileExistsError:
                pass


def del_dir():
    #str1 = "Delete a dir"
    #str2 = "Select local to create dir"
    #messagebox.showinfo(str1,str2)
    #messagebox.showinfo("Diretory", "Select dir to del")
    path = utils.select_path("Delete a dir", "Select a dir to delete.")
    if len(path) > 0:
        try:
            os.rmdir(path)
            print("Path removed", path)
        except FileExistsError:
            pass
