'''
Created on Jul 22, 2019

@author: arthurquites
'''
from main import Application
from tkinter import Tk

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.mainloop()