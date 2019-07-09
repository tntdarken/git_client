import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from subprocess import check_output

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # seta label
        self.labelMsg = ttk.Label(self)
        self.labelMsg["text"] = "Ola"
        self.labelMsg.pack()
        
        # seta o botão com uma ação
        self.hi_there = ttk.Button(self)
        self.hi_there["text"] = "Selecione uma pasta"
        self.hi_there["command"] = self.selecionar_pasta
        self.hi_there.pack(side="top")

        # seta o botão de sair // usando o TTK
        self.quit = ttk.Button(self, text="QUIT",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        # seta o tamanho da tela // master é uma variável da class pai Frame, que corresponde o objeto Tk()
        self.master.geometry("800x800")

        # seta o select
        var = tk.StringVar()
        var.set("Selecione") # Valor inicial
        option = ttk.OptionMenu(self, var, "one", "two", "three", "four")
        option.pack(side="left")

        ttk.Style().configure("TButton", padding=6, relief="flat",
        background="#ccc")

        ttk.Style().configure("TOptionMenu", padding=6, relief="flat",
        background="#ccc")

    # imprime a versão do git
    def git_version(self):
        print(check_output("git --version", shell=True))

    # abre o selecionador de diretórios
    def selecionar_pasta(self):
        directory = filedialog.askdirectory()
        print(directory)
        #filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

root = tk.Tk()
app = Application(master=root)
app.mainloop()

#from tkinter import ttk
#import tkinter

#root = tkinter.Tk()

#ttk.Style().configure("TButton", padding=6, relief="flat",
 #  background="#ccc")

#btn = tkinter.Button(text="Sample")
#btn.pack()

#btn = ttk.Button(text="Sample2")
#btn.pack()

#root.mainloop()

