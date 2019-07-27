'''
Created on Jul 19, 2019

@author: arthurquites
'''
from tkinter import *

def teste(content):
        # criar uma nova tela
        newwin = Toplevel()
        for msg in content.split('\\n'):
            display = Label(newwin, text=msg)
            display.pack() 