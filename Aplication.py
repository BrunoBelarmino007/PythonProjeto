from GUI import Gui
import Backend as core
from tkinter import END, messagebox

app = None
selected = None 

def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)

def search_command():
    app.listClientes.delete(0, END)
    rows = core.search( app.txtNome.get(),
                        app.txtSobrenome.get(),
                        app.txtEmail.get(),
                        app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)
