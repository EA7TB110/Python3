#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TKinter_01
Created on Fri Jul 11 09:58:40 2025

@author: manuelverdesalmeron

Crea una pantalla con un menu
    añade listbox y un scorllbar
    
"""

import tkinter as tk
from tkinter import messagebox
def nuevo_fichero():
    messagebox.showinfo("nuevo fichero", "nuevo fichero created!")

def open_fichero():
    messagebox.showinfo("Open fichero", "fichero opened!")

def exit_app():
    root.quit()

def cortar():
    messagebox.showinfo("cortar", "cortar selected!")

def copy():
    messagebox.showinfo("Copy", "Copy selected!")

def paste():
    messagebox.showinfo("Paste", "Paste selected!")


# Creando la ventana principal

root = tk.Tk()
root.title("Tkinter Ejemplo de Menu")
version = "V. 0.0"

def crear_listbox():
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)
    
    # Creando el listbox
    listbox = tk.Listbox(frame, height=30, width=100)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH) 
    
    # Creando el  Scrollbar y enlazandola con el Listbox
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    listbox.config(yscrollcommand=scrollbar.set)

def crear_pantalla():
    # Creando la barra del menu
    menu_bar = tk.Menu(root)
    
    
    # Creando el fichero de menus y añadiendo los comandos
    fichero_menu = tk.Menu(menu_bar, tearoff=0)
    fichero_menu.add_command(label="nuevo", command=nuevo_fichero)
    fichero_menu.add_command(label="Open", command=open_fichero)
    fichero_menu.add_separator()
    fichero_menu.add_command(label="Exit", command=exit_app)
    menu_bar.add_cascade(label="fichero", menu=fichero_menu)
    
    # Creando el menu edir y añadiendp los comandos
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="cortar", command=cortar)
    edit_menu.add_command(label="Copy", command=copy)
    edit_menu.add_command(label="Paste", command=paste)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)
    
    # Adjuntar la barra de menú a la ventana raíz
    root.config(menu=menu_bar)

crear_pantalla()
crear_listbox()

root.mainloop()