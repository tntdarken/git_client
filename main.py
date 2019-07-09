#'''
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from subprocess import check_output

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master, padding=(3,3,12,12))
        self.create_widgets()

    def create_widgets(self):
        namelbl = ttk.Label(self, text="Name")
        name = ttk.Entry(self)
        self.frame = ttk.Frame(self, borderwidth=5, relief="sunken", width=200, height=100)

        #onevar = BooleanVar()
        #twovar = BooleanVar()
        #threevar = BooleanVar()

        #onevar.set(True)
        #twovar.set(False)
        #threevar.set(True)

        #one = ttk.Checkbutton(self, text="One", variable=onevar, onvalue=True)
        #two = ttk.Checkbutton(self, text="Two", variable=twovar, onvalue=True)
        #three = ttk.Checkbutton(self, text="Three", variable=threevar, onvalue=True)
        sel_repositorio = ttk.Button(self, text="Selecionar repositório", command=self.selecionar_pasta)
        cancel = ttk.Button(self, text="Cancel")

        self.grid(column=0, row=0, sticky=(N, S, E, W))
        self.frame.grid(column=2, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
        namelbl.grid(column=0, row=0, columnspan=2, sticky=(N, W), padx=5)
        name.grid(column=0, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        #one.grid(column=0, row=3)
        #two.grid(column=1, row=3)
        #three.grid(column=2, row=3)
        sel_repositorio.grid(column=0, row=3)
        cancel.grid(column=1, row=3)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.rowconfigure(1, weight=1)
                
    # imprime a versão do git
    def git_version(self):
        print(check_output("git --version", shell=True))

    # abre o selecionador de diretórios
    def selecionar_pasta(self):
        directory = filedialog.askdirectory()
        print(directory)
        #filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

root = Tk()
app = Application(master=root)
app.mainloop()
#'''

###############################################

'''
from tkinter import ttk
import tkinter

root = tkinter.Tk()

ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")

btn = tkinter.Button(text="Sample")
btn.pack()

btn = ttk.Button(text="Sample2")
btn.pack()

root.mainloop()
'''

################################################

'''
from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(True)
twovar.set(False)
threevar.set(True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()
'''
