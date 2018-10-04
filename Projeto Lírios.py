from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook


class Main:
    def __init__(self, master):
        self.master = master
        self.abas = Notebook()
        self.frame_aba1 = Frame(self.abas)  # Aba superior 'Débitos'.
        self.frame_aba2 = Frame(self.abas)  # Aba 'REALIZAR PEDIDOS'.
        self.frame_aba3 = Frame(self.abas)  # Aba 'ENTREGAS'

        self.abas.add(self.frame_aba1, text='Débitos')  # Nomeando as abas.
        self.abas.add(self.frame_aba2, text='Realizar Pedido')  # Nomeando as abas.
        self.abas.add(self.frame_aba3, text='Entregas')  # Nomeando as abas.
        self.abas.pack(anchor=W)

        #  Início quadrado ADICIONAR DÉBITO.
        self.frame = LabelFrame(self.frame_aba1, text='ADICIONAR DÉBITO')
        self.frame.grid(row=0, column=0, padx=20, pady=20)

        Label(self.frame, text='Nome :').grid(row=1, column=1)
        self.name = Entry(self.frame)
        self.name.grid(row=1, column=2, padx=10)

        Label(self.frame, text='Data de Nascimento :').grid(row=2, column=1)
        self.datanasci = Entry(self.frame)
        self.datanasci.grid(row=2, column=2)

        Label(self.frame, text='CPF :').grid(row=3, column=1)
        self.cpf = Entry(self.frame)
        self.cpf.grid(row=3, column=2)

        Label(self.frame, text='Data do Débito :').grid(row=4, column=1)
        self.datdeb = Entry(self.frame)
        self.datdeb.grid(row=4, column=2)

        Label(self.frame, text='Valor do Débito :').grid(row=5, column=1)
        self.valordeb = Entry(self.frame)
        self.valordeb.grid(row=5, column=2)

        self.btn1 = Button(self.frame, text='ENVIAR', command=self.enviar_nome)
        self.btn1.grid(row=6, column=2, pady=10)

        # Início quadrado Buscar/Deletar Débitos.
        self.frame2 = LabelFrame(self.frame_aba1, text='BUSCAR/DELETAR DÉBITOS')
        self.frame2.grid(row=1, column=0)

        Label(self.frame2, text='Buscar por Nome :').grid(row=1, column=1)
        self.busnome = Entry(self.frame2)
        self.busnome.grid(row=1, column=2, padx=10)

        Label(self.frame2, text='Buscar por CPF :').grid(row=2, column=1)
        self.buscpf = Entry(self.frame2)
        self.buscpf.grid(row=2, column=2)

        Label(self.frame2, text='Buscar Pessoa').grid(row=3, column=1)

        Label(self.frame2, text='Deletar Débito').grid(row=3, column=2)

        self.btn2 = Button(self.frame2, text='BUSCAR')
        self.btn2.grid(row=4, column=1, pady=10)

        self.btn3 = Button(self.frame2, text='DELETAR', command=self.deletar_nome)
        self.btn3.grid(row=4, column=2)

        # Início tabela Treeview.

        self.tree = ttk.Treeview(self.frame_aba1, height=20, columns=('Nº', 'Nome', 'Valor do Débito', 'Data do Débito', 'CPF'))
        self.tree.grid(row=0, column=1, rowspan=10)
        self.tree.heading('#0', text='Nº', anchor=W)
        self.tree.heading('#1', text='Nome', anchor=W)
        self.tree.heading('#2', text='Valor do Débito', anchor=W)
        self.tree.heading('#3', text='Data do Débito', anchor=W)
        self.tree.heading('#4', text='CPF', anchor=W)
        self.tree.heading('#5', text='Data Nascimento', anchor=W)
        self.tree.column('#0', minwidth=50, width=80)
        self.tree.column('#1', minwidth=50, width=250)
        self.tree.column('#2', minwidth=50, width=150)
        self.tree.column('#3', minwidth=50, width=150)
        self.tree.column('#4', minwidth=100, width=200)
        self.tree.column('#5', minwidth=50, width=150)
        self.treeview = self.tree
        self.i = 1

        # Scrollbar da tabela Treeview.
        self.yscroll = Scrollbar(self.frame_aba1, orient=VERTICAL)
        self.tree['yscrollcommand'] = self.yscroll.set
        self.yscroll['command'] = self.tree.yview()
        self.yscroll.grid(row=0, column=1, rowspan=10, sticky=N+S+E)

    ############################## ABA REALIZAR PEDIDO #########################################

        self.frame3 = LabelFrame(self.frame_aba2, text='INFORMAÇÕES DO PEDIDO')
        self.frame3.grid(row=0, column=0, padx=10, pady=10)

        Label(self.frame3, text='Nome :').grid(row=0, column=0)
        self.nameframe3 = Entry(self.frame3)
        self.nameframe3.grid(row=0, column=1)

        Label(self.frame3, text='Entregar Dia :').grid(row=1, column=0)
        self.entdia = Entry(self.frame3)
        self.entdia.grid(row=1, column=1)

        Label(self.frame3, text='Endereço :').grid(row=0, column=2)
        self.ende = Entry(self.frame3)
        self.ende.grid(row=0, column=3)

        Label(self.frame3, text='Bairro :').grid(row=1, column=2)
        self.bairro = Entry(self.frame3)
        self.bairro.grid(row=1, column=3)

        Label(self.frame3, text='CEP :').grid(row=0, column=4)
        self.cep = Entry(self.frame3)
        self.cep.grid(row=0, column=5)

        Label(self.frame3, text='Ponto de Referência :').grid(row=1, column=4)
        self.pontodr = Entry(self.frame3)
        self.pontodr.grid(row=1, column=5)

        Label(self.frame3, text='Fone 1 :').grid(row=0, column=6)
        self.fone1 = Entry(self.frame3)
        self.fone1.grid(row=0, column=7)

        Label(self.frame3, text='Fone 2 :').grid(row=1, column=6)
        self.fone2 = Entry(self.frame3)
        self.fone2.grid(row=1, column=7, padx=10, pady=10)

        self.frame4 = LabelFrame(self.frame_aba2, text='INFORME AQUI OS PRODUTOS DO PEDIDO')
        self.frame4.grid(row=1, column=0)

        self.entradap = Text(self.frame4)
        self.entradap.grid(row=2, column=0, padx=10, pady=10)

        self.btn4 = Button(self.frame4, text='ENVIAR')
        self.btn4.grid(row=3, column=0, pady=10)

    # Comandos da aba Débitos
    def enviar_nome(self):
        self.treeview.insert('', 'end', text='Nº '+str(self.i), values=(self.name.get(), self.valordeb.get(),
                                                                       self.datdeb.get(), self.cpf.get(),
                                                                       self.datanasci.get()))
        self.name.delete(0, 'end')
        self.valordeb.delete(0, 'end')
        self.datdeb.delete(0, 'end')
        self.cpf.delete(0, 'end')
        self.datanasci.delete(0, 'end')
        self.i = self.i + 1

    def deletar_nome(self):
        self.selected_item = self.tree.selection()        # get selected item
        self.tree.delete(self.selected_item)


ins = Main
root = Tk()
Main(root)
root.title('Lírios Produtos de Limpeza')
root.wm_iconbitmap('lirios.ico')  # Create Logo
root.geometry('1366x768+0+0')
root.mainloop()
