from tkinter import *


class admins():
    '''
    funções dos admins
    '''
    def __init__(self, tl_admin):
        '''
        CONSTRUTOR PARA AS FUNÇÕES DOS ADMINS
        '''
       

#       LISTBOX DE TODOS OS USERS:
#       Criar uma listbox para mostrar os users
        self.tl_admin = tl_admin
        f = open('..\\Projeto_AED\\files\\users.txt', 'r')
        lines = f.readlines()        
        self.lbox_users= Listbox(self.tl_admin, height=10, selectmode='single', font=('Roboto', 14))
        for line in lines:
            self.lbox_users.insert(END, line) #END significa que cada line é inserida no fim do conteúdo da listbox
            self.lbox_users.place(x = 30, y = 240)
#       Criar um botãozinho para chamar a função de remover o user
        self.btn_remove_user = Button(self.tl_admin, text='Trash account', bg= '#ccc', fg='white', border = '0', padx=5, pady=5, font=('Roboto', 14), command=self.remove_account)
        self.btn_remove_user.place(x = 30, y = 480)
#   Função para remover o user selecionado
    def remove_account(self):
        '''
        Permite ao admin remover uma conta
        '''
        self.lbox_users.delete(self.lbox_users.curselection())
   


        
   

