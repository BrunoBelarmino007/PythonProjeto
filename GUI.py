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
