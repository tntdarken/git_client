from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from subprocess import check_output
from sys import platform
import json

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master, padding=(3,3,12,12))
        self.endRepo = ""
        self.config = {
            "currentRepo": ""
        }
        
        self.readConfig()
        
        root.geometry('800x600')
        
        #Configuração dos estilos
        s = ttk.Style()
        if platform == "darwin": # necessário para o mac, para sair do tema aqua
            s.theme_use('default')
        s.configure('Left.TFrame', background='grey')
        s.configure('Middle.TFrame', background='white')
        s.configure('Right.TFrame', background='grey')
        
        #Criação dos objetos
        f1 = ttk.Frame(root, style='Left.TFrame', width=0, height=0)
        f1.grid(row=0, column=0, sticky=(N,S,E,W))
        f2 = ttk.Frame(root,style='Middle.TFrame', width=0, height=0)
        f2.grid(row=0, column=1, sticky=(N,S,E,W))
        f3 = ttk.Frame(root,style='Right.TFrame', width=0, height=0)
        f3.grid(row=0, column=2, sticky=(N,S,E,W))
        
        self.tree = ttk.Treeview(f2)
        self.tree.bind("<Button-1>", self.onselect)
        self.tree.bind("<B1-Motion>", self.motion)
#         self.tree.bind("<<TreeviewSelect>>", self.onselectt)
        self.tree.grid(row=0, column=0, sticky=(N,S,E,W))
        self.showCommits()
#         people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
#         for p_id, p_info in people.items():
#             print("\nPerson ID:", p_id)
#             
#             for key in p_info:
#                 print(key + ':', p_info[key])
        self.treeFiles = ttk.Treeview(f3)
        self.treeFiles.bind("<Button-1>", self.onselectFile)
#         self.tree.bind("<<TreeviewSelect>>", self.onselectt)
        self.treeFiles.grid(row=0, column=0, sticky=(N,S,E,W))

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
        helpmenu.add_command(label="Mostrar Conteudo Commit", command=self.showCommitFiles)
        helpmenu.add_command(label="Mostrar nome repo", command=self.printRepoName)
        helpmenu.add_command(label="Abrir arquivo", command=self.readConfig)
        helpmenu.add_command(label="Escrever no arquivo", command=self.writeConfig)
        menubar.add_cascade(label="Help", menu=helpmenu)
        # display the menu
        root.config(menu=menubar)

        #Configuração da expansão dos elementos (se expande para ocupar a tela ou não)
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=2)
        root.columnconfigure(2, weight=1)
        root.rowconfigure(0, weight=1)
        f2.columnconfigure(0, weight=1)
        f2.rowconfigure(0, weight=1)

    def onExit(self):
        self.quit()
        
    def motion(self, evt):
        print(evt)
        
    def onselect(self, evt):
        item = self.tree.identify('item', evt.x, evt.y)
        self.showCommitFiles(self.tree.item(item), item)
#         print('O id do item clicado é ', item, ' e o resto é ', self.tree.item(item))

    def onselectFile(self, evt):
        item = self.treeFiles.identify('item', evt.x, evt.y)
        dados = self.treeFiles.item(item)
        self.showFileContent(dados['values'][0],item)
        
    def onselectt(self, event):
        real_coords = (self.tree.winfo_pointerx() - self.tree.winfo_rootx(),
                       self.tree.winfo_pointery() - self.tree.winfo_rooty())
        item = self.tree.identify('item', *real_coords)
        print('********** tree selection event **********')
        print('looks like this virtual event doesnt support event coordinates')
        print('event.x: %d, event.y: %d' % (event.x, event.y))
        print('real.x: %d, real.y: %d' % real_coords)
        print('clicked on', self.tree.item(item)['text'])
        print('******************************************\n')
        
    # imprime a versão do git
    def git_version(self):
        print(check_output("git --version", shell=True))
    
    def printRepoName(self):
        print(check_output("basename -s .git `git config --get remote.origin.url`", shell=True))
        
    # abre o selecionador de diretórios
    def selecionar_pasta(self):
        directory = filedialog.askdirectory()
        self.config['currentRepo'] = directory
        self.writeConfig()

    def showCommits(self):
        log = str(check_output('git log --pretty=format:"-* %h, %an, %ar, %s," --name-status -10', shell=True))
# --git-dir '+self.config['currentRepo']+'/.git
        for msg in log.replace('b\'-* ', '').split('-* '):
            commit = msg.split(', ')
            files = commit[3].split(',')
            files = files[1].replace('\\n','').replace('A\\t','-').replace('M\\t','-').replace('-','', 1).replace('\'', '').split('-')
            self.tree.insert("", 'end', commit[0], text=commit[1]+ " -> "+commit[3].split(',')[0], values=(files))
        
    def readConfig(self):
        f = open('config', 'r')
        for line in f:
            self.config = json.loads(line)
        f.close()
    
    def writeConfig(self):
        f = open('config', 'w')
        f.seek(0,2)
        f.write(json.dumps(self.config))
        f.close()
        
    def showCommitFiles(self, commit, id):
        self.treeFiles.delete(*self.treeFiles.get_children())
#         log = str(check_output('git --git-dir '+self.config['currentRepo']+'/.git diff --name-only '+commit, shell=True))
        for file in commit['values']:
            self.treeFiles.insert("", 'end', file, text=file, values=(id))


    def showFileContent(self, commit, file):
#         log = str(check_output('git diff '+commit+'~ '+commit, shell=True))
        log = str(check_output('git diff '+commit+' -- '+file, shell=True))
        # criar uma nova tela
        newwin = Toplevel(root)
        for msg in log.split('\\n'):
            display = Label(newwin, text=msg)
            display.pack() 
            
root = Tk()
app = Application(master=root)
app.mainloop()