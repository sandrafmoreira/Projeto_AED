from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from homepage import homepage_window #Para importar a função homepage_window (função que cria a janela homepage) que está no ficheiro homepage.py

#----------------------------------SIGN UP-----------------------------------------------------------

def go_back_sign_up(main_frame,sign_up_frame):
    """
    Função para quando o utilizador clica no botão 'Go Back', a janela volta á página principal
    """
    sign_up_frame.place_forget()
    main_frame.place(x = 0, y = 0)


def create_sign_up_frame( main_frame):
    """
    Função para mostrar o frame para o utilizador Criar Conta
    Neste frame, o utilizador cria uma conta com um nome de utilizador, o seu email, e a password
    """
    main_frame.place_forget()
    sign_up_background_image = Image.open('..\\Projeto_AED\\images\\backgrounds\\sign_up_background.jpg').resize((1000,600))
    image = ImageTk.PhotoImage(sign_up_background_image)
    sign_up_frame = Label(image=image)
    sign_up_frame.image = image
    sign_up_frame.place(x = 0, y = 0)

    sign_up_message = Label(sign_up_frame, text = 'Sign Up', font = ('Roboto', 55), bg = '#017BC9').place(x = 380, y = 80)

    email = StringVar()
    email.set('')
    email_label = Label(sign_up_frame, text = 'Email:', font = ('Roboto', 12), bg = '#14468C').place(x = 340, y = 250)
    email_entry = Entry(sign_up_frame, width = 25, font = ('Roboto', 12), textvariable = email).place(x = 400, y = 250)

    username = StringVar() #Variável do username que o utilizador inserir (mais tarde para criar conta)
    username.set('')
    username_label = Label(sign_up_frame, text = 'Username: ', font = ('Roboto', 12), bg = '#4F1174').place(x = 307, y = 300)
    username_entry = Entry(sign_up_frame, width = 25, font = ('Roboto', 12), textvariable = username).place(x = 400, y = 300)

    password = StringVar()
    password.set('')
    password_label = Label(sign_up_frame, text = 'Password:', font = ('Roboto', 12), bg = '#150233').place(x = 307, y = 350)
    password_entry = Entry(sign_up_frame, width = 25, font = ('Roboto', 12), textvariable = password, show ='*').place( x = 400, y = 350)

    confirm_password = StringVar()
    confirm_password.set('')
    confirm_password_label = Label(sign_up_frame, text = 'Confirmar Password:', font = ('Roboto', 12), bg = '#020031').place(x = 230, y = 400)
    confirm_password_entry = Entry(sign_up_frame, width = 25, font = ('Roboto', 12), textvariable = confirm_password, show ='*').place( x = 400, y = 400)

    #Botão para criar conta
    create_account_button = Button(sign_up_frame, text = 'Create Account', font = ('Roboto', 20), bg = '#020031', fg = 'white', bd = 2, command = lambda: create_account(email,username,password,confirm_password,main_frame,sign_up_frame)).place(x = 630, y = 450)

    #Botão para voltar à página principal
    go_back_button = Button(sign_up_frame, text = 'Go Back', font = ('Roboto', 20), bg = '#020031', fg = 'white', bd = 2, command = lambda:go_back_sign_up(main_frame,sign_up_frame)).place(x = 280, y = 450)


def create_account(email,username,password,confirm_password,main_frame,sign_up_frame):
    email = email.get()
    username = username.get()
    password = password.get()
    confirm_password = confirm_password.get()

    if email == '' or username == '' or password == '' or confirm_password == '':
        #Se o utilizador não tiver preenchido alguma das informações necessárias
        #Cria-se uma messagebox a mostrar um erro!
        messagebox.showerror('Error','You have to fill all the spaces!') #Cria-se uma messagebox a mostrar um erro!
        return #A função termina

    if password != confirm_password:
        #Se as passwords que o utilizador inseriu não forem iguais:
        #Cria-se uma messagebox a mostrar um erro!
        messagebox.showerror('Error','The passwords you inserted are not the same! \n Try again!') 
        return #A função termina
    
    if email.find('@') == -1:
        #Se o que o utilizador inseriu não tiver nenhum '@', não é um email!
        #Se for igual a -1 significa que não encontrou nenhum '@'!
        messagebox.showerror('Error','Insert a valid email!')
        return #A função termina
    
     #Abre-se o ficheiro onde estão presentes as informações dos utilizadores em modo leitura para verificar se o username que o utilizador inseriu já está presente no ficheiro
    f = open('..\\Projeto_AED\\files\\users.txt','r')
    conteudo = f.readlines() #Lê todo o conteudo presente no ficheiro 'users.txt'
    f.close() #Fecha o ficheiro

    for linhas in conteudo:
        """
        Ciclo for que percorre TODAS as linhas presentes na variavel 'conteudo' onde foi extraído todas as informações guardadas no ficheiro 'users.txt'
        """
        email_repetido = linhas[:linhas.find(';')]#Esta variável serve para buscar o user em cada linha para depois verificar se combina com o user que o utilizador inseriu
        if email == email_repetido:
            #Se for igual, mostra uma messagebox com um erro
            messagebox.showinfo('Try again!','The username you put is already in use! Try another one!') 
            return #A função termina
        user_repetido = linhas[linhas.find(';') + 1:linhas.rfind(';')] #Esta variável serve para buscar o email em cada linha para depois verificar se combina com o user que o utilizador inseriu
        if username == user_repetido:
            #Se for igual, mostra uma messagebox com um erro
            messagebox.showinfo('Try again!','The email you put has an account associated to it already!') 
            return #A função termina
        
    #Se nem o username e nem o username que o utilizador inseriu não estiverem no ficheiro, pode-se assim criar uma conta nova com as informações que o utilizador inseriu
    conteudo = email + ';' + username + ';' + password #A variável conteudo guarda o username, o email, e a password inseridos para depois inserir no ficheiro 

    #Abre o ficheiro 'utilizadores.txt' em modo append
    f = open('..\\Projeto_AED\\files\\users.txt','a')
    f.write(conteudo + '\n') #Escreve o que está guardado na variável conteudo 
    f.close() #Fecha o ficheiro

    #E mostra-se uma messagebox onde informa o utilizador que a conta foi criada com sucesso!! :DD
    messagebox.showinfo('Done!','You have sucessfully created an account in myPhotos! \n Login to start using the app! :)')
    go_back_sign_up(main_frame,sign_up_frame)

#----------------------------------LOGIN-----------------------------------------------------------

def go_back_login(main_frame,login_frame):
    """
    Função para quando o utilizador clica no botão 'Go Back', a janela volta á página principal
    """
    login_frame.place_forget()
    main_frame.place(x = 0, y = 0)


def create_login_frame(window, main_frame):
    main_frame.place_forget()
    login_background_image = Image.open('..\\Projeto_AED\\images\\backgrounds\\login_background.jpg').resize((1000,600))
    image = ImageTk.PhotoImage(login_background_image)
    login_frame = Label(image=image)
    login_frame.image = image
    login_frame.place(x = 0, y = 0)

    login_message = Label(login_frame, text = 'Login', font = ('Roboto', 55), bg = '#D26B58').place(x = 400, y = 150)

    username = StringVar() #Variável do username que o utilizador inserir para fazer login
    username.set('')
    username_label = Label(login_frame, text = 'Username:', font = ('Roboto', 12), bg = '#652F47').place(x = 305, y = 300)
    username_entry = Entry(login_frame, width = 25, font = ('Roboto', 12), textvariable = username).place(x = 400, y = 300)
    
    password = StringVar()
    password.set('')
    password_label = Label(login_frame, text = 'Password:', font = ('Roboto', 12), bg = '#582E46').place(x = 307, y = 350)
    password_entry = Entry(login_frame, width = 25, font = ('Roboto', 12), textvariable = password, show ='*').place( x = 400, y = 350)


    #Botão para criar conta
    login_button = Button(login_frame, text = 'Login', font = ('Roboto', 20), bg = '#3F2B47', fg = 'white', bd = 2, command = lambda: login(username,password,login_frame,window)).place(x = 580, y = 380)    


    #Botão para voltar à página principal
    go_back_button = Button(login_frame, text = 'Go Back', font = ('Roboto', 20), bg = '#3F2B47', fg = 'white', bd = 2, command = lambda:go_back_login(main_frame,login_frame)).place(x = 310, y = 380)

    
def login(username,password,login_frame,window):
    """
    Esta função junta as informações inseridas na frame de login \n
    Verifica se o username e password que o utilizador inseriu estão guardadas e corretas! \n
    Se não tiver, informa o utilizador o que está errado e/ou em falta
    """
    username = username.get()
    password = password.get() 

    #Se o utilizador não tiver inserido algum ou nenhum dos campos, mostra uma messagebox com erro
    if username == '' or password == '':
        messagebox.showerror('Erro','You have to fill all the spaces!')
        return #Termina-se a função

    #Abre-se o ficheiro 'users.txt' em modo leitura
    f = open('..\\Projeto_AED\\files\\users.txt','r')
    conteudo = f.readlines() #A variável 'conteudo' vai buscar toda a informação escrita no ficheiro
    f.close() #Fechar o ficheiro

    for linhas in conteudo:
        """
        Ciclo for que percorre TODAS as linhas de informação presentes na variável conteudo
        """
        #ADMINS
        if username == 'sandra' and password == '123' or username =='nuno' and password == '456' or username == 'ken' and password == '789':
            messagebox.showinfo('Sucess!','Welcome admin! :)')
            login_frame.place_forget()
            homepage_window(window)
            return

        verificar_username = linhas[linhas.find(';') + 1:linhas.rfind(';')] #Esta variável vai buscar o username presente em cada linha na variável 'conteudo'
        verificar_pass = linhas[(linhas.rfind(';') + 1):-1] #Esta variável vai buscar a password presente em cada linha na variável 'conteudo'

            #Se o username E password estiverem corretas, mostra-se uma messagebox a informar o utilizador que foi feito login com sucesso!
        if username == verificar_username and password == verificar_pass:
            messagebox.showinfo('Done!','You have sucessfully loged into the myPhotos! :)\n ')
            login_frame.place_forget()
            homepage_window(window)
            return
        
    #Se depois de ter percorrido a variável 'conteudo' toda e não ter-se encontrado as informações da conta:
    #Mostra-se uma messagebox de erro a informar o utilizador o ocorrido!
    if verificar_username != username or verificar_pass != password:
        messagebox.showerror('Error','The data you inserted in incorrect, try again!')
