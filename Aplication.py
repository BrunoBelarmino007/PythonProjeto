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

def insert_command():
    cpf = app.txtCPF.get().strip()
    
    # Verifica se CPF está vazio
    if not cpf:
        messagebox.showerror("Erro", "CPF é obrigatório!")
        return
    
    # Tenta inserir o cliente
    success = core.insert(app.txtNome.get(),
                         app.txtSobrenome.get(),
                         app.txtEmail.get(),
                         cpf)
    
    if success:
        # Limpa os campos após inserção bem-sucedida
        app.entNome.delete(0, END)
        app.entSobrenome.delete(0, END)
        app.entEmail.delete(0, END)
        app.entCPF.delete(0, END)
        view_command()
        messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")
    else:
        messagebox.showerror("Erro", "CPF já existe no sistema!")

def update_command():
    if selected:
        success = core.update(selected[0],
                            app.txtNome.get(),
                            app.txtSobrenome.get(),
                            app.txtEmail.get(),
                            app.txtCPF.get())
        
        if success:
            view_command()
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
        else:
            messagebox.showerror("Erro", "CPF já existe em outro registro!")

def del_command():
    if selected:
        id = selected[0]
        core.delete(id)
        view_command()

def getSelectedRow(event):
    global selected
    try:
        index = app.listClientes.curselection()[0]
        selected = app.listClientes.get(index)
        
        app.entNome.delete(0, END)
        app.entNome.insert(END, selected[1])
        
        app.entSobrenome.delete(0, END)
        app.entSobrenome.insert(END, selected[2])
        
        app.entEmail.delete(0, END)
        app.entEmail.insert(END, selected[3])
        
        app.entCPF.delete(0, END)
        app.entCPF.insert(END, selected[4])
    except IndexError:
        # Nenhum item selecionado
        pass
    
    return selected