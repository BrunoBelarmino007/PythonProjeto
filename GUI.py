from tkinter import *

class Gui(): 
    """
        Classe da Interface Gráfica
    """
    
    def __init__(self):
        self.x_pad = 5
        self.y_pad = 3
        self.width_entry = 30

        self.window = Tk()
        self.window.wm_title("PYSQL version 1.0")

        # variáveis de entrada
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # labels
        self.lblnome = Label(self.window, text="Nome:")
        self.lblsobrenome = Label(self.window, text="Sobrenome:")
        self.lblemail = Label(self.window, text="Email:")
        self.lblcpf = Label(self.window, text="CPF:")

        # entradas
        self.entNome = Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entEmail = Entry(self.window, textvariable=self.txtEmail, width=self.width_entry)
        self.entCPF = Entry(self.window, textvariable=self.txtCPF, width=self.width_entry)
