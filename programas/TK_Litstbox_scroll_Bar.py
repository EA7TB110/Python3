#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 09:58:40 2025

@author: manuelverdesalmeron

Crea una listbox con una anchura de 100 y una altura de 30
asociado a ella hay un scrolbar a la izquierda

"""

import tkinter as tk
from tkinter import messagebox

# Creando la ventana principal
root = tk.Tk()
root.title("Tkinter Listbox Ejemplo")


version = "V. 0.0"
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Creando el listbox
listbox = tk.Listbox(frame, height=30, width=100)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Add items to the Listbox
for i in range(50):
    listbox.insert(tk.END, f"Item {i+1}")

# Creando el  Scrollbar y enlazandola con el Listbox
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()