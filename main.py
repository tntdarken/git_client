#'''
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from subprocess import check_output

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master, padding=(3,3,12,12))
        self.endRepo = ""
        
        #Configuração dos estilos
        s = ttk.Style()
        s.configure('Myy.TFrame', background='blue')
        s.configure('My.TFrame', background='red')

        #Criação dos objetos
        f1 = ttk.Frame(root, style='My.TFrame', width=10, height=100)
        f1.grid(row=0, column=0, sticky="nsew")
        f2 = ttk.Frame(root,style='Myy.TFrame', width=10, height=100)
        f2.grid(row=0, column=1, sticky=(N,S,E,W))

        menubar = Menu(root)
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.selecionar_pasta)
        filemenu.add_command(label="Save", command=self.git_version)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        # create more pulldown menus
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut", command=self.git_version)
        editmenu.add_command(label="Copy", command=self.git_version)
        editmenu.add_command(label="Paste", command=self.git_version)
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.printEnd)
        menubar.add_cascade(label="Help", menu=helpmenu)
        # display the menu
        root.config(menu=menubar)

        #Configuração da expansão dos elementos (se expande para ocupar a tela ou não)
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=1)

    def onExit(self):
        self.quit()
        
    # imprime a versão do git
    def git_version(self):
        print(check_output("git --version", shell=True))

    # abre o selecionador de diretórios
    def selecionar_pasta(self):
        directory = filedialog.askdirectory()
        self.endRepo = directory
        #filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

    def printEnd(self):
        print(self.endRepo)
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
